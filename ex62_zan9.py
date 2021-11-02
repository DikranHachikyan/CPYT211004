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

if __name__ == '__main__':
    # 2. променлива от тип Point
    # клас - типа, обект - променлива от типа, представител на класа
    p1 = Point()
    p2 = Point(30, 50)
    print(f'Point:({p1.x},{p1.y})')

    p1.draw()
    p2.draw()
    p2.move_to(30, -10)
    p2.draw()
    
    print('---')