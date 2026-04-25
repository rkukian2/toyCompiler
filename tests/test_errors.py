"""Verify the MiniCError hierarchy from SCOPE §8 is importable, raisable,
and that every subclass is catchable as MiniCError.
"""

import pytest

import minic
from minic.errors import (
    MiniCControlFlowError,
    MiniCDynamicShapeError,
    MiniCError,
    MiniCInPlaceOpError,
    MiniCShapeError,
    MiniCUnsupportedDTypeError,
    MiniCUnsupportedOpError,
)

ALL_ERRORS = [
    MiniCUnsupportedOpError,
    MiniCUnsupportedDTypeError,
    MiniCDynamicShapeError,
    MiniCControlFlowError,
    MiniCShapeError,
    MiniCInPlaceOpError,
]


def test_base_is_exception() -> None:
    assert issubclass(MiniCError, Exception)


@pytest.mark.parametrize("cls", ALL_ERRORS)
def test_subclass_of_base(cls: type[MiniCError]) -> None:
    assert issubclass(cls, MiniCError)


@pytest.mark.parametrize("cls", ALL_ERRORS)
def test_can_raise_with_message(cls: type[MiniCError]) -> None:
    with pytest.raises(cls, match="boom"):
        raise cls("boom")


@pytest.mark.parametrize("cls", ALL_ERRORS)
def test_caught_as_minic_error(cls: type[MiniCError]) -> None:
    with pytest.raises(MiniCError):
        raise cls("any subclass should be catchable as MiniCError")


def test_reexported_from_top_level() -> None:
    assert minic.MiniCError is MiniCError
    assert minic.MiniCShapeError is MiniCShapeError
