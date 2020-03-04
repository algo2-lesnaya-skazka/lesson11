from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
mc.player.setPos(pos.x, pos.y, pos.z)
type = 103
for i in range(5):
    for j in range(4):
        for k in range(7):
            mc.setBlock(pos.x+i, pos.y+j, pos.z+k, type)
