import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def perimeter_c(self):
        return 2 * math.pi * self.r

    def area_c(self):
        return math.pi * (self.r ** 2)

    def intersection_c(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if distance >= self.r + other.r:
            return "Окружности не пересекаются"
        if distance <= abs(self.r - other.r):
            return math.pi * min(self.r, other.r) ** 2

        r1, r2 = self.r, other.r
        seg1 = r1 ** 2 * math.acos((distance ** 2 + r1 ** 2 - r2 ** 2) / (2 * distance * r1))
        seg2 = r2 ** 2 * math.acos((distance ** 2 + r2 ** 2 - r1 ** 2) / (2 * distance * r2))
        seg3 = 0.5 * math.sqrt((-distance + r1 + r2) * (distance + r1 - r2) * (distance - r1 + r2) * (distance + r1 + r2))

        return seg1 + seg2 - seg3


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def perimeter_r(self):
        return self.h * 2 + self.w * 2

    def area_r(self):
        return self.h * self.w

    def diag(self):
        return math.sqrt(self.h ** 2 + self.w ** 2)

    def intersection_r(self, other):
        l1 = self.x - self.w / 2
        r1 = self.x + self.w / 2
        t1 = self.y - self.h / 2
        b1 = self.y + self.h / 2

        l2 = other.x - other.w / 2
        r2 = other.x + other.w / 2
        t2 = other.y - other.h / 2
        b2 = other.y + other.h / 2

        if r1 <= l2 or r2 <= l1 or b1 <= t2 or b2 <= t1:
            return "Прямоугольники не пересекаются"

        x_overlap = max(0, min(r1, r2) - max(l1, l2))
        y_overlap = max(0, min(b1, b2) - max(t1, t2))

        return x_overlap * y_overlap


rect1 = Rectangle(100, 100, 50, 80)
rect2 = Rectangle(120, 130, 60, 40)

print(f"Площадь rect1: {rect1.area_r()}")
print(f"Площадь rect2: {rect2.area_r()}")

print(f"Периметр rect1: {rect1.perimeter_r()}")
print(f"Периметр rect2: {rect2.perimeter_r()}")

print(f"Диагональ rect1: {rect1.diag()}")
print(f"Диагональ rect1: {rect2.diag()}")

intersection_area_rect = rect1.intersection_r(rect2)
print(f"Площадь пересечения прямоугольников: {intersection_area_rect}")

rect3 = Rectangle(100, 100, 50, 80)
rect4 = Rectangle(200, 200, 60, 40)

print(f"Площадь пересечения прямоугольников: {rect3.intersection_r(rect4)}")

circle1 = Circle(200, 200, 50)
circle2 = Circle(240, 250, 40)

print(f"Площадь circle1: {circle1.area_c():.2f}")
print(f"Площадь circle2: {circle2.area_c():.2f}")

print(f"Длина окружности circle1: {circle1.perimeter_c():.2f}")
print(f"Длина окружности circle2: {circle2.perimeter_c():.2f}")

intersection_area_circle = circle1.intersection_c(circle2)
print(f"Площадь пересечения кругов: {intersection_area_circle:.2f}")

circle3 = Circle(200, 200, 50)
circle4 = Circle(300, 300, 40)

print(f"Площадь пересечения кругов: {circle3.intersection_c(circle4)}")

