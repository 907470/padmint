import importlib.util
import json
from pathlib import Path
import shlex
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('prepare_asm_processor', HERE / 'prepare.py')
producer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(producer)


class PrepareTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'source'; self.source.mkdir()
        self.output = self.root / 'prepared'
        self.originals = {
            'build.py': b'# unchanged entry point\n',
            'asm_processor.py': b'''import tempfile
def assemble(assembler, s_name, o_name):
    ret = os.system(assembler + " " + s_name + " -o " + o_name)
    if ret != 0:
        raise RuntimeError("failed to assemble")
''',
            'prelude.inc': b'# unchanged assembly prelude\n',
            'LICENSE': b'unchanged upstream license\n',
        }
        self.lock = {'commit': 'synthetic-pinned-source', 'files': {},
                     'patched_sha256': producer.digest(producer.patch_process(self.originals['asm_processor.py']))}
        for name, data in self.originals.items():
            (self.source / name).write_bytes(data)
            self.lock['files'][name] = {'size': len(data), 'sha256': producer.digest(data)}
        self.save_lock()
        here = patch.object(producer, 'HERE', self.root)
        here.start(); self.addCleanup(here.stop)

    def save_lock(self):
        (self.root / 'inputs.json').write_text(json.dumps(self.lock), encoding='utf-8')

    def test_prepare_preserves_inputs_license_and_entry_point(self):
        result = producer.prepare(self.source, self.output)
        self.assertEqual(result, self.output / 'build.py')
        for name, original in self.originals.items():
            self.assertEqual((self.source / name).read_bytes(), original)
            if name != 'asm_processor.py':
                self.assertEqual((self.output / name).read_bytes(), original)
        receipt = json.loads((self.output / 'provenance.json').read_text())
        self.assertEqual(receipt['source_commit'], self.lock['commit'])
        self.assertEqual(receipt['files']['asm_processor.py'], self.lock['patched_sha256'])

    def test_modified_source_fails_before_output_created(self):
        (self.source / 'LICENSE').write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'Pinned source mismatch: LICENSE'):
            producer.prepare(self.source, self.output)
        self.assertFalse(self.output.exists())

    def test_missing_source_fails_before_output_created(self):
        (self.source / 'prelude.inc').unlink()
        with self.assertRaises(FileNotFoundError):
            producer.prepare(self.source, self.output)
        self.assertFalse(self.output.exists())

    def test_preexisting_output_is_preserved(self):
        self.output.mkdir(); preserved = self.output / 'keep'; preserved.write_bytes(b'old work')
        with self.assertRaises(FileExistsError):
            producer.prepare(self.source, self.output)
        self.assertEqual(list(self.output.iterdir()), [preserved])
        self.assertEqual(preserved.read_bytes(), b'old work')

    def test_changed_patch_output_fails_before_writing(self):
        self.lock['patched_sha256'] = '0' * 64; self.save_lock()
        with self.assertRaisesRegex(ValueError, 'Patched source checksum mismatch'):
            producer.prepare(self.source, self.output)
        self.assertFalse(self.output.exists())

    def test_arguments_round_trip_without_shell_and_failure_is_kept(self):
        producer.prepare(self.source, self.output)
        namespace = {}; exec((self.output / 'asm_processor.py').read_bytes(), namespace)
        arguments = [r'C:\Tools with spaces\as.exe', '-EB', "quote'and;$(no-shell)"]
        assembler = ' '.join(shlex.quote(arg) for arg in arguments)
        with patch.object(namespace['subprocess'], 'call', return_value=0) as call:
            namespace['assemble'](assembler, 'input with spaces.s', 'output with spaces.o')
            call.assert_called_once_with(arguments + ['input with spaces.s', '-o', 'output with spaces.o'])
        with patch.object(namespace['subprocess'], 'call', return_value=1):
            with self.assertRaisesRegex(RuntimeError, 'failed to assemble'):
                namespace['assemble'](assembler, 'input.s', 'output.o')


if __name__ == '__main__':
    unittest.main()
