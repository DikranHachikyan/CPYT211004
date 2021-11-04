# 1. дефиниция на класа

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


if __name__ == '__main__':
    # 2. променлива от тип Point
    # клас - типа, обект - променлива от типа, представител на класа
    p = Point(10,20)

    print(f'Point ({p.x},{p.y})')
    p.x = 120
    p.y = 130

    p.draw()

    print('---')