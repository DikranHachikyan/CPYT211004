# 1. дефиниция на класа

class Point():
    
    def __init__(self):
        print('Point Ctor')
        # данни обекта
        self.x = 10
        self.y = 20

    def draw(self):
        print(f'draw point at ({self.x},{self.y})')


if __name__ == '__main__':
    # 2. променлива от тип Point
    # клас - типа, обект - променлива от типа, представител на класа
    p = Point()
    
    print(f'Point:({p.x},{p.y})')

    p.draw()
    
    print('---')