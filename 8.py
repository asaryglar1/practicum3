import math

def angles(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами не существует"
    A = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    B = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
    C = math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
    return(A, B, C)

a = float(input())
b = float(input())
c = float(input())
print(angles(a, b, c)[0])
print(angles(a, b, c)[1])
print(angles(a, b, c)[2])