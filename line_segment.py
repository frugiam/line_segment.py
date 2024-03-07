# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 03/06/2024
# Description: Project 9

class Point:
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def distance_to(self, other_point):
        x1, y1 = self._x_coord, self._y_coord
        x2, y2 = other_point.get_x_coord(), other_point.get_y_coord()
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return distance


class LineSegment:
    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        return self._endpoint_1

    def get_endpoint_2(self):
        return self._endpoint_2

    def length(self):
        return self._endpoint_1.distance_to(self._endpoint_2)

    def is_parallel_to(self, other_line_segment):
        slope1 = self.slope()
        slope2 = other_line_segment.slope()
        return abs(slope1 - slope2) < 0.000001

    def slope(self):
        x1, y1 = self._endpoint_1.get_x_coord(), self._endpoint_1.get_y_coord()
        x2, y2 = self._endpoint_2.get_x_coord(), self._endpoint_2.get_y_coord()

        if x2 - x1 == 0:
            # Avoid division by zero for vertical lines
            return float('inf')
        else:
            return (y2 - y1) / (x2 - x1)