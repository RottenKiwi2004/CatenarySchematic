import mcschematic
from Vector3 import Vector3
import math


def drawLine(pos1: Vector3, pos2: Vector3) -> list[Vector3]:

    """
    :param pos1: Position 1
    :param pos2: Position 2
    :return: List of Vector3 where blocks need to be placed
    """

    subVector = 2
    blockList = []

    lineVec = pos2 - pos1
    length = lineVec.magnitude()

    currentPos = pos1
    stepVec = lineVec / length / subVector
    for _ in range(math.ceil(length) * subVector):

        currentPos += stepVec
        blockList.append(round(currentPos))

    return blockList



# p1 = Vector3(0, 0, 0)
# p2 = Vector3(3, 4, 12)
#
# drawLine(p1, p2)