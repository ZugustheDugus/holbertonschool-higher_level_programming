#!/usr/bin/python3
"""
Square class, inheriting from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class created from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Init Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print method"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update method for object attrs"""
        flag = 0
        if args is not None:
            flag = 1
        if len(args) > 0 and flag == 1:
            self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Square's attrs"""
        attrs = {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
        return attrs

    @property
    def size(self):
        """size getter"""
        return super().width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
