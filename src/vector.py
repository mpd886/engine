import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = self._calc_magnitude()

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        if not isinstance(other, Vector):
            return True
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def _calc_magnitude(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def normalized(self):
        """
        :return: normalized version of vector
        """
        return Vector(self.x/self.magnitude,
                      self.y/self.magnitude,
                      self.z/self.magnitude)

    def dot(self, v1):
        """Calculate dot product between this and given vector
        """
        return self.x*v1.x + self.y*v1.y + self.z*v1.z

    def cross(self, v1):
        """Calulate cross product between this and given vector
        :returns: a new Vector
        """
        return Vector(self.y*v1.z - self.z*v1.y,
                      self.z*v1.x - self.x*v1.z,
                      self.x*v1.y - self.y*v1.x)

    def angle_between(self, v1):
        """Returns the angle (in radians) between this and the given vector
        """
        dot = self.dot(v1)
        mag = self.magnitude*v1.magnitude
        return math.acos(dot/mag)
