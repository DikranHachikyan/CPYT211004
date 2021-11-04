# 1. дефиниция на класа

from math import sqrt

class A:
    pass

class Point():
    
    def __init__(self, x=0, y=0, *args, **kwargs):
        print('Point Ctor')
        # данни обекта
        self.x = x
        self.y = y

    def draw(self):
        print(f'draw point at ({self.x},{self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        assert type(x) is int and x >= 0, 'x must be positive int number'
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert type(y) is int and y >= 0, 'y must be positive int number'
        self.__y = y

    # Function Overriding
    def __str__(self):
        return f'({self.x},{self.y})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        raise TypeError('expected instance of Point')    

    def __gt__(self, other):
        if not isinstance(other, Point):
            raise TypeError('expected instance of Point')    

        dx1 = self.x ** 2 
        dy1 = self.y ** 2
        dist1 = sqrt(dx1 + dy1)
        
        dx2 = other.x ** 2 
        dy2 = other.y ** 2
        dist2 = sqrt(dx2 + dy2)

        return dist1 > dist2

    def __add__(self,other):
        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
        elif isinstance(other, (int,float)):
            new_x = self.x + other
            new_y = self.y + other    
        else:
            raise TypeError('expected instance of Point')    
        return Point(new_x, new_y)
        
    def __del__(self):
        print('Object Dtor')


if __name__ == '__main__':
    # 2. променлива от тип Point
    # клас - типа, обект - променлива от типа, представител на класа
    p = Point(10,20)

    print(f'Point ({p.x},{p.y})')
    p.x = 120
    p.y = 130

    p.draw()

    print(f'Point:{p}')

    p2 = Point(120,130)

    if p2 == p:
        print(f'{p2} equals to {p}')
    else:
        print(f'{p2} not equals to {p}')

    p.x = 10
    p.y = 20

    if p2 > p:
        print(f'{p2} > {p}')
    else:
        print(f'{p2} <= {p}')

    
    p3 = p2 + p

    print(f'Point 3:{p3}')

    p4 = p2 + 5
    print(f'Point 4:{p4}')
    print('---')