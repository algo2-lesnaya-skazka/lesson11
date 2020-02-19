# Python часть

Урок 11:<br> 
Списки
страницы 128-129

Задачи<br>
https://stepik.org/lesson/253733/step/1?unit=234411

Python 3 загрузка<br>
https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe<br>

Установка библиотеки для Minecraft<br>
MCPI<br>
https://pypi.org/project/mcpi/<br>

pip install mcpi<br>

Простая программа подключения<br>
<pre><code>from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Hello minecraft world")
x = 0
y = 120
z = 0
mc.player.setPos(x, y, z)
</code></pre>

Использование модуля time<br>
<pre><code>time.sleep(2)</code></pre>

Получение координат игрока<br>
<pre><code>
pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) +" z=str(pos.z))
</code></pre>
Установка блока по координатам<br>
<pre><code>
x = 0
y = 120
z = 0
type = 103
mc.setBlock(x, y, z, type)
</code></pre>

Установка редактора

Visual Studio Code<br>
https://code.visualstudio.com/Download

Настройка русского языка
Russian - Language Russian Pack - Configure Display Language

Minecraft Server Spigot<br>
https://yadi.sk/d/sWB4zISgEpGIaQ

TLauncher<br>
https://tlauncher.org/installer

Книга Python<br>
https://yadi.sk/d/1KWhK7OMs4j4Sw

Книга minecraft python<br>
https://yadi.sk/d/Ts-piLxJKiibqg


