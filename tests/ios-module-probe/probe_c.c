/* C, optimized: Apple's string.h and stdio.h then use their fortified forms
   (secure/_string.h, secure/_strings.h, secure/_stdio.h), as BlueWake's runtime does. */
#undef NDEBUG  /* Exercise assert's C declaration even in the Release probe. */
#include <assert.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <sys/mman.h>

static_assert(sizeof(void *) == 8, "iOS modules are 64-bit");

__attribute__((visibility("default"))) int padmint_module_probe_c(char *out, unsigned long size, int value) {
    assert(out != NULL);
    char buffer[32];
    memset(buffer, 0, sizeof buffer);
    snprintf(buffer, sizeof buffer, "padmint %d", value);
    memcpy(out, buffer, size < sizeof buffer ? size : sizeof buffer);
    return (int)strlen(buffer) + (int)ldexp(1.0, value & 3);
}

__attribute__((visibility("default"))) int padmint_module_probe_mapping(void) {
    const size_t size = 4096;
    void *region = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANON, -1, 0);
    if (region == MAP_FAILED) return -1;
    ((char *)region)[0] = 42;
    return munmap(region, size);
}
