// Phase 0 spike: trivial kernel that exercises the C-ABI contract
// from ARCHITECTURE.md §6 (extern "C", float* buffers, int64 size,
// row-major layout, no allocations, no Python callbacks).
#include <cstdint>

extern "C" void add_f32(const float* a, const float* b, float* out, std::int64_t n) {
    for (std::int64_t i = 0; i < n; ++i) {
        out[i] = a[i] + b[i];
    }
}
