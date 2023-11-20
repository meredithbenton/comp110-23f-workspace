"""Combining two lists into a dictionary."""

__author__ = "730657068"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Zip together a list of strings and integers."""
    dictionary = {}
    if len(keys) != len(values):
        return {}
    if len(keys) == 0 or len(values) == 0:
        return {}
    else:
        for elem in range(len(keys)):
            dictionary[keys[elem]] = values[elem]
    return dictionary