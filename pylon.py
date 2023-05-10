from line import drawLine
from Vector3 import Vector3
from random import randint as rand

import mcschematic
schem = mcschematic.MCSchematic()

def placeBlocks(blocks: list[Vector3], blockName: str) -> None:

    for block in blocks:
        # print(block.tupleInt())
        schem.setBlock(block.tupleInt(), blockName)

def pylon(origin: Vector3, layers: int, layerHeight: float, size: float, rotation = 0) -> list[Vector3]:

    blockPos = []

    # Position vector
    basePos = [
        Vector3(size / 2, 0, size / 2),
        Vector3(-size / 2, 0, size / 2),
        Vector3(-size / 2, 0, -size / 2),
        Vector3(size / 2, 0, -size / 2)
    ]

    topY = layerHeight * layers
    topSize = size / 8
    topSize = topSize if topSize > 5 else 5

    # Position vector
    topPos = [
        Vector3(topSize, topY, topSize),
        Vector3(-topSize, topY, topSize),
        Vector3(-topSize, topY, -topSize),
        Vector3(topSize, topY, -topSize)
    ]

    # The actual vector representing four legs
    legVectors = []
    for i in range(4):
        legVectors.append(topPos[i] - basePos[i])
        blockPos.extend(drawLine(basePos[i], topPos[i]))

    # Position vector of each layer for 4 corners
    layerVectors = []
    for i in range(layers + 1):
        layer = []
        for j in range(4):
            leg = legVectors[j]
            layer.append(leg * i / layers + basePos[j])
        layerVectors.append(layer)

    # Position middle vector of each layer
    layerMiddleVectors = []
    for l in layerVectors:
        layer = []
        for i in range(4):
            pos = l[i].lerp( l[(i+1) % 4], 0.5)
            layer.append(pos)
            blockPos.extend(drawLine(l[i], l[(i + 1) % 4]))
            schem.setBlock(pos.tupleInt(), "minecraft:diamond_block")
        layerMiddleVectors.append(layer)

    for i in range(1, layers + 1):
        for j in range(4):
            # print(layerMiddleVectors[i][j], " -> ",layerVectors[i+1][j])
            blockPos.extend(drawLine(layerMiddleVectors[i][j], layerVectors[i-1][j]))
            blockPos.extend(drawLine(layerMiddleVectors[i][j], layerVectors[i-1][(j+1) % 4]))

    for layer in layerVectors:
        print(layer)


    return blockPos




placeBlocks(pylon(Vector3(0, 0, 0), 6, 20, 20), "minecraft:iron_block")
schem.setBlock((0, 0, 0), "minecraft:diamond_block")
schem.save("C:\\Users\\Asus\\AppData\\Roaming\\.minecraft\\schematics\\MCSchematic", f"drawPylon", mcschematic.Version.JE_1_18_2)