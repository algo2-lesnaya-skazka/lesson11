from mcpi.minecraft import Minecraft
mc = Minecraft.create(address='localhost', port=4711)
mc.postToChat("Hello minecraft world")
pos = mc.player.getPos()
#mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) +" z="+str(pos.z))