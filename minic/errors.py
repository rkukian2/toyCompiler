"""User-visible exceptions raised by MiniC.

Every error inherits from MiniCError so users can catch them all with one
clause. Each subclass marks a specific failure mode from SCOPE §8.
"""


class MiniCError(Exception):
    """Base class for every MiniC error."""


class MiniCUnsupportedOpError(MiniCError):
    """The model uses an op outside the supported set (SCOPE §1)."""


class MiniCUnsupportedDTypeError(MiniCError):
    """A tensor uses a dtype outside the supported set (SCOPE §2)."""


class MiniCDynamicShapeError(MiniCError):
    """A tensor's shape cannot be determined at trace time (SCOPE §4)."""


class MiniCControlFlowError(MiniCError):
    """The traced region contains data-dependent control flow (SCOPE §4)."""


class MiniCShapeError(MiniCError):
    """Input shapes do not satisfy an op's shape rule (SCOPE §1)."""


class MiniCInPlaceOpError(MiniCError):
    """An in-place op was used in the traced region (SCOPE §4)."""
