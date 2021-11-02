# 1. дефиниция на класа

class Point():
    
    def __init__(self, x=0, y=0, *args, **kwargs):
        print('Point Ctor')
        # данни обекта
        self.__x = x
        self.__y = y

    def draw(self):
        print(f'draw point at ({self.__x},{self.__y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def set_x(self, x):
        assert type(x) is int and x >= 0, 'x must be positive int number'
        self.__x = x

    def get_x(self):
        return self.__x

if __name__ == '__main__':
    # 2. променлива от тип Point
    # клас - типа, обект - променлива от типа, представител на класа
    p = Point(10,20)

    # print(f'Point:({p.__x}, {p.__y})')
    # p.__x = -30
    # p.__y = 40

    p.set_x(30)
    print(f'Point x = {p.get_x()}')
    
    print('---')