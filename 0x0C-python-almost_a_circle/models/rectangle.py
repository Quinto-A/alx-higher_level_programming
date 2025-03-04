#!/usr/bin/python3

"""a class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """"class rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """creates a new Rectangle instance"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """overrides the __str__ method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            attr_list = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the class Rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
            }
