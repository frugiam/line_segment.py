# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 03/06/2024
# Description: Project 9

"'Create the Point class with private data members, x_coord and y_coord.'"
class Point:
    def __init__(self, x, y):
        self._x_coord = x
        self._y_coord = y

"'Add get methods for x_coord and y_coord.'"
    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

"'Add a distance_to method to calculate the distance between two Point objects.'"
    def distance_to(self, other_point):
        return ((self._x_coord - other_point.get_x_coord()) ** 2 + (
                    self._y_coord - other_point.get_y_coord()) ** 2) ** 0.5

"'Create the LineSegment class with private data members, endpoint_1 and endpoint_2.'"
class LineSegment:
    def __init__(self, point_1, point_2):
        self._endpoint_1 = point_1
        self._endpoint_2 = point_2

"'Add get methods for endpoint_1 and endpoint_2.'"
    def get_endpoint_1(self):
        return self._endpoint_1

    def get_endpoint_2(self):
        return self._endpoint_2

"'Add a length method that calculates the distance between the two endpoints.'"
    def length(self):
        return self._endpoint_1.distance_to(self._endpoint_2)

"'Add a slope method to calculate the slope of the LineSegment.'"
    def slope(self):
        return (self._endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord()) / (self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord())

"'Add an is_parallel_to method to check if two LineSegments are parallel.'"
    def is_parallel_to(self, other_line_segment):
        return self.slope() == other_line_segment.slope()
