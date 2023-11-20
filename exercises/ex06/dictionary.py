"""Add meaningful docstring once I understand the purpose of this file."""

__author__ = "730657068"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the list."""
    inv_dict = {}
    for letter in input:
        number = input[letter]
        inv_dict[number] = letter
    if len(input) != len(inv_dict):
        raise KeyError("Cannot have duplicate values in input.")
    return inv_dict


def favorite_color(list: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    color_count: dict[str, int] = {}
    fav_color: str = ""
    max_number = 0
    for element in list:
        if list[element] in color_count:
            color_count[list[element]] += 1
        else:
            color_count[list[element]] = 1
    for elem in color_count:
        if color_count[elem] > max_number:
            max_number = color_count[elem]
            fav_color = elem
    return fav_color


def count(inp_list: list[str]) -> dict[str, int]:
    """Returns the number of times each value appears in a list."""
    count_dict: dict[str, int] = {}
    for value in inp_list:
        if value in count_dict:
            count_dict[value] += 1
        else: 
            count_dict[value] = 1
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Groups words by letter."""
    alph: dict[str, list[str]] = {}
    for word in word_list:
        first_letter = word[0].lower()
        if first_letter in alph:
            alph[first_letter].append(word)
        else: 
            alph[first_letter] = [word]
    return alph


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Mutates a dict with days of the week and students who attended class."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
    return attendance_log