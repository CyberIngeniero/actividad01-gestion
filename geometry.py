#! usr/bin bash
import abc  # Abstract Base Class
from math import pi


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def circumference(self):
        pass

    def __str__(self):
        return type(self).__name__


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def circumference(self):
        return 2 * pi * self.r


class Rectangle(Shape):
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def area(self):
        return self.l * self.w

    def circumference(self):
        return 2 * self.l + 2 * self.w


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

# class A
class A(object):
    def __init__(self, _foo, _bar):
        self._foo = _foo
        self._bar = _bar
        self.lorem = 'lorem'

    def foo(self):
        print(f'foo: {self._foo}')

    def bar(self):
        print(f'bar: {self._bar}')


# class B
class B(object):
    def __init__(self, _value):
        self.value = _value

    def show(self):
        print(f'value: {self.value}')

# class C
class C(object):
    def __init__(self, _value):
        self.value = _value

    def show(self):
        print(f'value: {self.value}')

if __name__ == '__main__':
    shapes = [Square(10), Circle(20), Rectangle(3.4, 1.5)]

    for shape in shapes:
        print(f'{shape} area is {shape.area()}')

    a = A(1, 2)
    a.foo()
    a.bar()
    print(a.lorem)

    b = B(3)
    b.show()

    c = C(4)
    c.show()