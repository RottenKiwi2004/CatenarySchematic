import math
from Vector3 import Vector3
from line import drawLine


def catenary_function(start: Vector3, end: Vector3, length: float, percent: float) -> Vector3:

    ######################################

    def findConstantA(h: float, v: float, l: float) -> float:

        ######################################
        def f(param: float) -> float:
            return math.sqrt(l * l - v * v) - 2 * param * math.sinh(h / 2 / param)
        ######################################

        step = 1
        targetVal = 1

        # Find max value only if the result is still in negative zone
        if f(targetVal) < 0:
            while f(targetVal) < 0:
                targetVal += step
                step *= 2

        # Binary Search (after entering positive zone, minimise the error)
        step /= 2
        currentValue = f(targetVal)
        while math.fabs(currentValue) > 0.0000001:

            if currentValue < 0:
                targetVal += step

            if currentValue > 0:
                targetVal -= step

            step /= 2
            currentValue = f(targetVal)

        return targetVal

    ######################################

    def findConstantM(x: float, y: float, a: float) -> float:

        p = math.e ** (x/a)

        # AtomThum derived this monstrosity, please don't mind me for an evil piece of mess
        return a * math.log( ( (2*y*p) - math.sqrt(4 * y**2 * p**2 + 4 * a**2 * p * (1-p)**2 ) ) / ( 2 * a * (1-p) ) )

    ######################################

    distVec = end - start
    x, y, z = distVec.tuple()

    dist = distVec.magnitude()
    h = math.sqrt(x * x + z * z)
    v = y
    a = findConstantA(h, v, length)
    m = findConstantM(h, v, a)
    n = -a * math.cosh(m/a)

    newX = h * percent
    newY = a * (math.cosh((newX - m) / a) - math.cosh(m / a))

    zeroDegVector = Vector3(1, 0, 0)
    destDegVector = Vector3(x, 0, z)

    angle = destDegVector.angle(zeroDegVector)

    # Apply the rotation matrix (using Linear Algebra)
    return start + Vector3(newX * math.cos(angle), newY, newX * math.sin(angle))


def catenary(start: Vector3, end: Vector3, sagPercent: float) -> list[Vector3]:

    blockList = []

    distVec = end - start
    dist = distVec.magnitude()
    length = dist * (1 + sagPercent)
    stepCount = math.ceil(length) * 2

    if sagPercent < 0.05:

        unitVec = distVec / distVec.magnitude() / 2

        for i in range(stepCount):

            blockList.append(start + unitVec * i)

        return blockList

    else:

        for i in range(stepCount):

            percent = i / stepCount
            blockList.append(catenary_function(start, end, length, percent))

        return blockList


def drawCatenary(start: Vector3, end: Vector3, sagPercent: float) -> list[Vector3]:

    pointList = catenary(start, end, sagPercent)
    pointCount = len(pointList)

    drawList = []

    for i in range(pointCount - 1):
        drawList.extend(drawLine(pointList[i], pointList[i + 1]))

    return drawList
