import unittest
import math
import vector


class VectorTests(unittest.TestCase):
    def test_magnitude(self):
        v = vector.Vector(2, -2, -2)
        self.assertEqual(3.4641016151377544, v.magnitude)

    def test_normalized(self):
        v = vector.Vector(2, -2, -2)
        normalized = v.normalized()
        self.assertEqual(0.5773502691896258, normalized.x)
        self.assertEqual(-0.5773502691896258, normalized.y)
        self.assertEqual(-0.5773502691896258, normalized.z)

    def test_dot(self):
        v1 = vector.Vector(10, 10, 10)
        v2 = vector.Vector(32, 17, 100)
        expected = 1490
        result = v1.dot(v2)
        self.assertEqual(expected, result)

    def test_eq(self):
        v1 = vector.Vector(1, 2, 3)
        v2 = vector.Vector(1, 2, 3)
        self.assertTrue(v1 == v2)

    def test_eq_notequals(self):
        v1 = vector.Vector(1, 2, 3)
        v2 = vector.Vector(2, 2, 3)
        self.assertFalse(v1 == v2)

    def test_ne(self):
        v1 = vector.Vector(1, 2, 3)
        v2 = vector.Vector(2, 2, 3)
        self.assertTrue(v1 != v2)

    def test_ne_equalobjects(self):
        v1 = vector.Vector(1, 2, 3)
        v2 = vector.Vector(1, 2, 3)
        self.assertFalse(v1 != v2)

    def test_cross(self):
        v1 = vector.Vector(2, 3, 4)
        v2 = vector.Vector(4, 3, 2)
        expected = vector.Vector(-6, 12, -6)
        self.assertEqual(expected, v1.cross(v2))

    def test_angle_between(self):
        v1 = vector.Vector(1, 2, 3)
        v2 = vector.Vector(4, 5, 6)
        expected = 0.22572613
        self.assertAlmostEqual(expected, v1.angle_between(v2), 8)

    def test_ninety_degress_angle(self):
        v1 = vector.Vector(0, 1, 0)
        v2 = vector.Vector(1, 0, 0)
        expected = math.pi / 2
        self.assertEqual(v1.angle_between(v2), expected)

    def test_180_degrees(self):
        v1 = vector.Vector(-1, 0, 0)
        v2 = vector.Vector(1, 0, 0)
        self.assertEqual(v1.angle_between(v2), math.pi)

    def test_add(self):
        v1 = vector.Vector(1, 1, 1)
        v2 = vector.Vector(3, 4, 5)
        self.assertEqual(vector.Vector(4, 5, 6), v1 + v2)