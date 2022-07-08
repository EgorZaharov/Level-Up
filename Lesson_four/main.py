# from Lesson_four import sum_n
# a=int(input())
# b=int(input())
# print(sum_n(a,b))

# from Lesson_four import calendar_check
# x = int(input('Введите целое число от 1 до 12:'))
# y = 0
# y = calendar_check(x)
# print(y)

from figures.circle import perimeter_circle, square_circle

r = int(input('Введите радиус:'))
p = perimeter_circle(r)
s = square_circle(r)
print (f"Периметр круга = {p} мм")
print (f"Площадь круга = {s} мм2")

from figures.triangle import perimeter_triangle, square_triangle

a = int(input('Введите длину первой стороны треугольника:'))
b = int(input('Введите длину второй стороны треугольника:'))
c = int(input('Введите длину третьей стороны треугольника:'))
x = perimeter_triangle(a,b,c)
y = square_triangle(a,b,c)
print (f"Периметр треугодника = {x} мм")
print (f"Площадь круга = {y} мм2")

from figures.rectangle import perimeter_rectangle, square_rectangle

a = int(input('Введите длину первой стороны прямоугольника:'))
b = int(input('Введите длину второй стороны прямоугольника:'))
q = perimeter_rectangle(a,b)
w = square_rectangle(a,b)
print (f"Периметр треугодника = {q} мм")
print (f"Площадь круга = {w} мм2")