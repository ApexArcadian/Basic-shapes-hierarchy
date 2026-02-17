from abc import ABC, abstractmethod

class BasicShape(ABC):
    def __init__(self, name='Shape'):
        self._area = 0.0
        self._name = name
    
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, value):
        self._area = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @abstractmethod
    def calc_area(self):
        pass


class Circle(BasicShape):
    def __init__(self, x, y, r, n='Circle'):
        super().__init__(n)
        self._x_center = x
        self._y_center = y
        self._radius = r
        self.calc_area()
    
    @property
    def x_center(self):
        return self._x_center
    
    @property
    def y_center(self):
        return self._y_center
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        self.calc_area()
    
    def calc_area(self):
        import math
        self._area = math.pi * (self._radius ** 2)
        return self._area


class Rectangle(BasicShape):
    def __init__(self, l, w, n='Rectangle'):
        super().__init__(n)
        self._length = l
        self._width = w
        self.calc_area()
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        self._length = value
        self.calc_area()
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        self.calc_area()
    
    def calc_area(self):
        self._area = self._length * self._width
        return self._area


class Square(Rectangle):
    def __init__(self, s, n='Square'):
        self._side = s
        super().__init__(s, s, n)
        self.name = n
    
    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, value):
        self._side = value
        self._length = value
        self._width = value
        self.calc_area()
