# импорт без __init__.py
# from draw.point import Point


# импорт с __init__.py

from draw import Point

if __name__ == '__main__':

    p1 = Point(10,20)
    p2 = Point(10,20)
    p3 = Point(10,20)

    del p2
    print(f'count:{Point.count}')
   
    print('---')