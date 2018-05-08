from random import *
color_1 = ["红","黄","绿","蓝","黑","白"]

color_2 = ["红","黄","绿","蓝","黑","白"]

color1 = ""
color2 = ""
count = 0
def getBall(color,n):
    color1 = color_1[n]
    color2 = color_2[n]
for i in range(6):
    getBall(color_1,i)
    if color1 == "红":
        color_2.remove(color1)
        for j in range(5):
            getBall(j)
            count += 1




