import pygame
import random
import math
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
screen = pygame.display.set_mode((710,1530))
with open('highscore.txt') as f:
	highscore = f.read()
	

#creating buttons
def buttons(button_x,button_y,msg):
	button = pygame.image.load('switch.jpg')
	screen.blit(button,(button_x,button_y))
	st = pygame.font.Font('freesansbold.ttf', 124) 
	text = st.render(msg,True,(255,25,255))
	screen.blit(text,(button_x+132,button_y+200))
	pygame.display.update() 

#--game intro
def intro():
	intro = True 
	introback = pygame.image.load('introback.jpg')
	screen.blit(introback,(0,0))
	buttons(50,200,'PLAY')
	buttons(50,800,'QUIT')
	
	while intro:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
			pos = pygame.mouse.get_pos()
			if (pos[0]>50 and pos[0]<50+500) and (pos[1]>350 and pos[1]<=200+350):
				game()
			if (pos[0]>50 and pos[0]<50+500) and (pos[1]>950 and pos[1]<=800+350):
				pygame.quit()
				quit()
			
			hi = pygame.font.SysFont(None,63)
			high = hi.render(f'highscore : {highscore}',True,(255,255,255))
			screen.blit(high,(30,1450))
		pygame.display.update()
	

#game-main

def game():
	control_key = pygame.image.load('control_key.png')
	clock = pygame.time.Clock()
	FPS = 60
	text = pygame.font.Font('freesansbold.ttf', 36)
	score = 0
	v = 1.5
	
	#--exit button
	exit = pygame.image.load('exit.png')
	
	
	#--score
	def score_():
		score_f = text.render(f'score -: {score}',True,(5,10,0))
		screen.blit(score_f,(500,1450))
	
	
	#-- creating food
	food_number = 6
	random_x = []
	random_y = []
	for i in range(food_number):
		random_x.append(random.randint(70,600))
		random_y.append(random.randint(90,1000))
	food = pygame.image.load('food.png')
	
	#-- creating player
	player_x = random.randint(70,600)
	player_y = random.randint(90,1000)
	player_x_change = 0
	player_y_change = 0
	
	def player_(player_x,player_y):
		pygame.draw.circle(screen , (170,20,50) , (player_x,player_y),20)
		
		
	#-- collision
	def collision(player_x,player_y,random_x,random_y,i):
		distance = math.sqrt(((random_x - player_x)**2)+((random_y - player_y)**2))
		return distance < i
		
		
	#--snake length
	size_list = []
	length_check = 1
	def length(size_list):
		for x,y in size_list:
			pygame.draw.circle(screen,(17,10,50),(x ,y),15)
	
	#--game over
	def game_over():
		over = text.render('GAME OVER',True,(255,0,0))
		screen.blit(over ,(300,400))		
	
	#--highscore
	with open('highscore.txt') as f:
		highscore = f.read()
	
	quit = False 
	while not quit:
		
		screen.fill((110,120,170))
		
		
		screen.blit(control_key,(239,1200))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True
				
		#--control_key functionality
			pos = pygame.mouse.get_pos()
			if (pos[0] > 310 and pos[0] < 400) and (pos[1] > 1200 and pos[1] < 1270):
				player_y_change = -v	
			#	player_x_change = 0
				
			if (pos[0] > 400 and pos[0] < 475) and (pos[1] > 1270 and pos[1] < 1370):
				player_x_change = v
			#	player_y_change = 0
				
			if (pos[0] > 235 and pos[0] < 300) and (pos[1] > 1270 and pos[1] < 1370):
				player_x_change = -v	
			#	player_y_change = 0
				
			if (pos[0] > 310 and pos[0] < 400) and (pos[1] > 1370 and pos[1] < 1445):
				player_y_change = v		
			#	player_x_change = 0
			
		#-- collision
		for i in range(food_number):		
			if collision(player_x,player_y,random_x[i]+10,random_y[i]+17,20):
				
				random_x[i] = random.randint(70,600)
				random_y[i] = random.randint(90,1000)
				length_check += 5
				score += 1
				if score > int(highscore):
					highscore = str(score)
				if score%10 == 0:
				    v = v+0.3
				
					
		player_x += player_x_change
		player_y += player_y_change
		
		ini_player = []
		ini_player.append(player_x)
		ini_player.append(player_y)
		size_list.append(ini_player)
		
		
		
		#-- screen boundary
		if player_x >= 670:
			player_x = 670
			
		
		if player_x <= 45:
			player_x = 45
	
		if player_y >= 1130:
			player_y = 1130
		
		if player_y <= 55:
			player_y = 55
			
		
		
		
		
		
		pygame.draw.rect(screen,(0,0,0),(10,20,700,1150))
		pygame.draw.rect(screen,(40,100,0),(20,30,680,1130))
		
		
		
		length(size_list)
		player_(player_x,player_y)
		
		
		for i in range(food_number):
			screen.blit(food,(random_x[i],random_y[i]))
		
		
		score_()
		
		if player_x >= 670 or player_x <= 45 or player_y >= 1130 or player_y <= 55:
			v = 0
			game_over = pygame.font.Font('freesansbold.ttf', 90)
			g_text = game_over.render('GAME OVER',True,(55,0,100))
			ret = game_over.render('retry',True,(255,250,255))
			screen.blit(g_text,(70,400))
			screen.blit(ret,(250,950))
		
			with open('highscore.txt','w') as up:
				up.write(highscore)
				
				
			if (pos[0]>250 and pos[0]<450) and (pos[1]>950 and pos[1]< 1030):
					v = 3
					game()
					
				
		else:
			if len(size_list) > length_check:
				size_list.pop(0)
		screen.blit(exit,(30,1350))
		pp = pygame.mouse.get_pos()
		if (pp[0]>30 and pp[0]<30+128) and (pp[1]>1350 and pp[1]<=1350+128):
				intro()

			
		pygame.display.update()
		clock.tick(FPS)
	
		
intro()


