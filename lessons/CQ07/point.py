"""CQ07: Intro to Object Oriented Programming."""

from __future__ import annotations


class Point:
    """This is my point class."""
    x: float = 0.0
    y: float = 0.0

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Takes input and assigns those as initial values for x and y."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Mutates a point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point."""
        new_pt_x = self.x * factor
        new_pt_y = self.y * factor
        return Point(new_pt_x, new_pt_y)
    
    def __str__(self) -> str:
        """Returns point in string format."""
        point = f"x: {self.x}; y: {self.y}"
        return point
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplies point by a factor."""
        new_pt_x = self.x * factor
        new_pt_y = self.y * factor
        return Point(new_pt_x, new_pt_y)
    
    def __add__(self, factor: int | float) -> Point:
        """Multiplies point by a factor."""
        new_pt_x = self.x + factor
        new_pt_y = self.y + factor
        return Point(new_pt_x, new_pt_y)