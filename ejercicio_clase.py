import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def compute_distance(self, other_point):
        return math.sqrt((self._x - other_point.get_x())**2 + (self._y - other_point.get_y())**2)


class Line:
    def __init__(self, start_point, end_point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, start_point):
        self._start_point = start_point
        self._length = self.compute_length()

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, end_point):
        self._end_point = end_point
        self._length = self.compute_length()

    def get_length(self):
        return self._length

    def compute_length(self):
        return self._start_point.compute_distance(self._end_point)


class Shape:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = self._compute_edges()

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        self._vertices = vertices
        self._edges = self._compute_edges()

    def _compute_edges(self):
        edges = []
        for i in range(len(self._vertices)):
            start = self._vertices[i]
            end = self._vertices[(i + 1) % len(self._vertices)]
            edges.append(Line(start, end))
        return edges

    def compute_area(self):
        raise NotImplementedError("Debe ser implementado en la subclase")

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)


class Rectangle(Shape):
    def __init__(self, bottom_left, top_right):
        self._bottom_left = bottom_left
        self._top_right = top_right
        vertices = [
            bottom_left,
            Point(top_right.get_x(), bottom_left.get_y()),
            top_right,
            Point(bottom_left.get_x(), top_right.get_y())
        ]
        super().__init__(vertices)

    def compute_area(self):
        width = self._top_right.get_x() - self._bottom_left.get_x()
        height = self._top_right.get_y() - self._bottom_left.get_y()
        return width * height


class Square(Rectangle):
    def __init__(self, bottom_left, side_length):
        self._side_length = side_length
        top_right = Point(bottom_left.get_x() + side_length, bottom_left.get_y() + side_length)
        super().__init__(bottom_left, top_right)

    def compute_area(self):
        return self._side_length ** 2

    def compute_perimeter(self):
        return 4 * self._side_length


#Ejemplo de uso:
bottom_left = Point(0, 0)
top_right = Point(4, 3)
rect = Rectangle(bottom_left, top_right)
print(f"Area del Rectangulo: {rect.compute_area()}")
print(f"Perimetro del Rectangulo: {rect.compute_perimeter()}")

square = Square(Point(1, 1), 2)
print(f"Area del Cuadrado: {square.compute_area()}")
print(f"Perimetro del cuadrado: {square.compute_perimeter()}")