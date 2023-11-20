"""dict Unit Tests."""


__author__ = "730657068"


from exercises.ex06.dictionary import invert

from exercises.ex06.dictionary import favorite_color

from exercises.ex06.dictionary import alphabetizer

from exercises.ex06.dictionary import update_attendance

from exercises.ex06.dictionary import count


def test_invert_1() -> None:
    """Invert test works as expected."""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert_2() -> None:
    """When given nothing, invert test returns nothing."""
    assert invert({}) == {}


def test_invert_3() -> None:
    """Invert test works with numbers."""
    assert invert({"1": "a", "2": "b", "3": "c"}) == {"a": "1", "b": "2", "c": "3"}


def test_favorite_color_1() -> None:
    """Favorite color test works as expected."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == 'blue'


def test_favorite_color_2() -> None:
    """When given nothing, favorite color test returns nothing."""
    assert favorite_color({}) == ''


def test_favorite_color_3() -> None:
    """Gives last color between the two when there is a tie between colors."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Bob": "green", "Matilda": "green", "Everett": "yellow"}) == "yellow"


def test_count_1() -> None:
    """Count works as expected."""
    assert count([1, 2, 4, 3, 2, 4, 3, 3, 2, 1]) == {1: 2, 2: 3, 4: 2, 3: 3}


def test_count_2() -> None:
    """When given nothing, count returns nothing."""
    assert count([]) == []


def test_count_3() -> None:
    """Count works with negative numbers."""
    assert count([-2, 3, 3, -1, -2, 4]) == {-2: 2, 3: 2, -1: 1, 4: 1}


def test_alphabetizer_1() -> None:
    """Alphabetizer works as expected."""
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_2() -> None: 
    """Alphabetizer works when some words have capital letters."""
    assert alphabetizer(["Python", "sugar", "Turtle", "party", "table"]) == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def test_alphabetizer_3() -> None:
    """When given nothing, alphabetizer returns nothing."""
    assert alphabetizer([]) == []


def test_update_attendance_1() -> None:
    """Update attendance works as expected."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(attendance_log, "Tuesday", "Vrinda") == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_2() -> None:
    """When no names are added to the attendance dict, the dict remains the same."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(attendance_log, "", "") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}


def test_update_attendance_3() -> None:
    """When a repeat name is added to the dict, the dict remains the same."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(attendance_log, "Monday", "Vrinda") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}