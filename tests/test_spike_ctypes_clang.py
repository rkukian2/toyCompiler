"""Phase 0 spike: prove we can compile a .cpp with clang++, load with
ctypes.CDLL, and call it with row-major float* buffers per ARCHITECTURE.md §6.
"""

import ctypes
import shutil
import subprocess
from pathlib import Path

import pytest

SPIKE_SRC = Path(__file__).resolve().parent.parent / "spikes" / "ctypes_clang" / "add_kernel.cpp"


@pytest.fixture(scope="module")
def add_fn(tmp_path_factory: pytest.TempPathFactory):
    if shutil.which("clang++") is None:
        pytest.skip("clang++ not on PATH")

    build_dir = tmp_path_factory.mktemp("spike_ctypes_clang")
    so_path = build_dir / "add_kernel.so"

    subprocess.run(
        [
            "clang++",
            "-O3",
            "-march=native",
            "-shared",
            "-fPIC",
            "-o",
            str(so_path),
            str(SPIKE_SRC),
        ],
        check=True,
    )

    lib = ctypes.CDLL(str(so_path))
    fn = lib.add_f32
    fn.argtypes = [
        ctypes.POINTER(ctypes.c_float),
        ctypes.POINTER(ctypes.c_float),
        ctypes.POINTER(ctypes.c_float),
        ctypes.c_int64,
    ]
    fn.restype = None
    return fn


def test_add_f32_elementwise(add_fn) -> None:
    n = 8
    FloatArr = ctypes.c_float * n
    a = FloatArr(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0)
    b = FloatArr(0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5)
    out = FloatArr()

    add_fn(a, b, out, n)

    expected = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]
    assert list(out) == pytest.approx(expected)


def test_add_f32_row_major_2d(add_fn) -> None:
    # Verify the row-major contract: a tensor of shape (M, N) at (i, j)
    # lives at offset i * N + j. We add two MxN buffers and check.
    M, N = 3, 4
    n = M * N
    FloatArr = ctypes.c_float * n
    a = FloatArr(*[float(i * N + j) for i in range(M) for j in range(N)])
    b = FloatArr(*[100.0 for _ in range(n)])
    out = FloatArr()

    add_fn(a, b, out, n)

    for i in range(M):
        for j in range(N):
            assert out[i * N + j] == pytest.approx(100.0 + i * N + j)
