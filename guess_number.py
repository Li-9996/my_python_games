import random
num=random.randint(1,100)
print("我想了个1-100的数字,来猜吧!")
while True:
	guess=int(input("你猜:"))
	if guess<num:
		print("小了!")
	elif guess>num:
		print("大了!")
	else:
		print("猜对啦!就是", num)
		break