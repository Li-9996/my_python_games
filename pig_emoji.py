 # -*- coding: utf-8 -*-
import time
pig="🐷"
track=["_" for _ in range(40)]
position=0
print("准备开始! 小猪要跑到终点啦! ")
time.sleep(1)
while position<len(track)-1:
	print("\n"*20)
	position+=1
	for i in range(len(track)):
		if i==position:
			print(pig,end="")
		else:
			print("_",end="")
	print()
	time.sleep(0.5)
print("\n恭喜!小猪跑到终点了!👏 ")
input("按 Enter 键关闭窗口...")
