from line import drawLine
from Vector3 import Vector3
from random import randint as rand
from catenary import drawCatenary

import mcschematic

schem = mcschematic.MCSchematic()

pos1 = Vector3(216, 210, -189)
pos2 = Vector3(328, 236, -244)

def placeBlocks(blocks: list[Vector3], blockName: str) -> None:

    for block in blocks:
        # print(block.tupleInt())
        schem.setBlock(block.tupleInt(), blockName)


placeBlocks(drawCatenary(pos1, pos2, 0.1), "minecraft:glowstone")

schem.save("C:\\Users\\Asus\\AppData\\Roaming\\.minecraft\\schematics\\MCSchematic", f"drawCatenary", mcschematic.Version.JE_1_18_2)


