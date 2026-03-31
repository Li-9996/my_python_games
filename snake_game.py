import random
import time
import os
import msvcrt
# 初始化游戏
WIDTH=20
HEIGHT=10
snake=[(5,5),(5,4),(5,3)]  # 蛇的身体,(y,x)
direction = 'RIGHT'
food = (random.randint(0,HEIGHT-1),random.randint(0,WIDTH-1))
score = 0

def clear_screen():
	os.system('cls' if  os.name == 'nt'  else  'clear' )

# 键盘方向
while True:
	if msvcrt.kbhit():
		key = msvcrt.getch()
		if key == b'w'  or key == b'W':
			if direction != 'DOWN':
				direction = 'UP'
		elif key == b's'  or  key == b'S':
			if direction != 'UP':
				direction = 'DOWN'
		elif key ==b'a'  or key ==b'A':
			if direction!= 'RIGHT':
				direction = 'LEFT'
		elif key ==b'd'  or key ==b'D':
			if direction!= 'LEFT':
				direction = 'RIGHT'
	clear_screen()
	
	# 游戏画面
	for y in range(HEIGHT):
		for x in range(WIDTH):
			if (y,x) == snake[0]:
				print('0', end='')  #蛇头
			elif (y,x) in snake:
				print('o', end='')  #蛇身
			elif (y,x) == food:
				print('*', end='')  #食物
			else:
				print(' ', end='')  #空地
		print()
	print(f"得分 🏆 : {score} | 控制方向:W(上) A(左) S(下) D(右)")
	
	# 移动蛇
	head_y, head_x = snake[0]
	if direction == 'UP':
		new_head = (head_y - 1, head_x)
	elif direction == 'DOWN':
		new_head = (head_y + 1, head_x)
	elif direction == 'LEFT':
		new_head = (head_y, head_x - 1)
	elif direction == 'RIGHT':
		new_head = (head_y, head_x + 1)
	
	# 碰撞测试 (撞墙/撞自己判断)
	if (new_head[0] < 0 or new_head[0] >=HEIGHT or
		new_head[1] < 0 or new_head[1] >=WIDTH or
		new_head in snake[1:]):
		clear_screen()
		print(f"游戏结束💀!最终得分: {score}")
		input("按ENTER退出游戏...")
		break

	snake.insert(0,new_head)
	
	# 吃食物  
	if new_head == food :
		score += 10
	
	#确保食物不在蛇身上	
	while food in snake:  
			food = (random.randint(0,HEIGHT-1), random.randint(0, WIDTH-1))
	else:
		snake.pop()  #没吃到就去掉尾巴,实现移动
	
	time.sleep(0.3)