"""Challenge Question."""

__author__ = "730657068"


def w_sum(vals: list[float]) -> float:
    """Add together values in vals."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Add together values in vals."""
    sum: float = 0.0
    for value in vals:
        sum += value
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Add together values in vals."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum