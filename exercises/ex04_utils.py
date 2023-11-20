"""EX04 - 'list' Utility Functions."""


def all(int_list: list[int], input_int: int) -> bool:
    """Returns whether or not every integer in the list matches the given integer."""
    if len(int_list) == 0:
        return False
    list_index = len(int_list) - 1
    while list_index >= 0:
        if str(int_list[list_index]) == str(input_int):
            list_index -= 1
        else: 
            return False
    return True


def max(max_list: list[int]) -> int:
    """Returns the maximum integer in a list."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_index: int = (len(max_list) - 1)
    max_int: int = max_list[max_index]
    while max_index >= 0:
        if max_list[max_index] > max_int:
            max_int = max_list[max_index]
        max_index -= 1
    return max_int


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns whether each number at each index is equal."""
    if len(list_1) != len(list_2):
        return False
    check_index = 0
    while check_index < len(list_1):
        if list_1[check_index] == list_2[check_index]:
            check_index += 1
        else:
            return False
    return True