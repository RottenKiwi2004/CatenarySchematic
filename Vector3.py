from __future__ import annotations
import math

class Vector3:

    def __init__(self, x: float, y: float, z: float):

        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, key):

        match key:
            case 0:
                return self.x
            case 1:
                return self.y
            case 2:
                return self.z

    def normalised(self) -> Vector3:
        return self / self.magnitude()

    def cross(self, other: Vector3) -> Vector3:
        newX = self.y * other.z - self.z * other.y
        newY = self.z * other.x - self.x * other.z
        newZ = self.x * other.y - self.y * other.x
        return Vector3(newX, newY, newZ)

    def dot(self, other: Vector3) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self) -> float:
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

    def angle(self, other: Vector3) -> float:
        w = Vector3(self[1] * other[2] - self[2] * other[1], self[2] * other[0] - self[0] * other[2], self[0] * other[1] - self[1] * other[0])
        signed = 1
        if w[1] < 0:
            signed = -1
        return math.acos(self.normalised().dot(other.normalised())) * signed

    def tuple(self) -> tuple[float, float, float]:
        return self.x, self.y, self.z

    def tupleInt(self, n=0) -> tuple[int, int, int]:
        return math.floor(self.x), math.floor(self.y), math.floor(self.z)

    def __add__(self, other: Vector3) -> Vector3:
        return Vector3(self.x + other.x, self.y + other.y, + self.z + other.z)

    def __radd__(self, other: Vector3):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return other + (-self)

    def __truediv__(self, other: float):
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __repr__(self):
        return f"[{self.x}]\t[{self.y}]\t[{self.z}]"

    def __round__(self, n=0):
        return Vector3(round(self.x, n), round(self.y, n), round(self.z, n))

