"""Test my zip function."""

__author__ = "730657068"

from lessons.zip import zip


def test_lists_not_empty_use() -> None:
    """Tests that an empty list returns an empty bracket."""
    assert zip([], []) == {}


def test_lists_different_length() -> None:
    """Tests that lists of different length return an empty bracket."""
    assert zip(["Monday", "Tuesday", "Wednesday"], [1, 2]) == {}


def test_correct_formatting() -> None:
    """Tests that there are no repeats in keys."""
    assert zip(["Monday", "Tuesday", "Wednesday"], [1, 2, 3]) == {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3}