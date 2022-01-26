import pygame
import random

pygame.init()   # Initiating the pygame module (Optional but a good practice)
W=500
H=500

WIN=pygame.display.set_mode((W,H))#Setting the initial Screen Dimension
pygame.display.set_caption("SNAKE GAME")

snake_x=W//2#Initiating the x and y coordinates of the snake to half of the window parameters
snake_y=H//2
del_x=0
del_y=0
fud_x,fud_y=random.randint(0,W),random.randint(0,H)#Initiating a random interger value between 0 and the Width or height of the screen as the x and y of the food respectively
snake_body=[(snake_x,snake_y)]#Creating the body of the snake as list and adding the initial position to it as a tuple


def draw_snake():    #Function to draw the snake from the snake_body list to the screen
	for body in snake_body:
		pygame.draw.rect(WIN,(255,255,255),[body[0],body[1],10,10])

def snake_move():    #Function to move the snake in the screen
	global snake_x,snake_y
	snake_y=(snake_y+del_y)%H
	snake_x=(snake_x+del_x)%W
	snake_body.append((snake_x,snake_y))

def draw_fud():# Function that draws food to the screen
	pygame.draw.rect(WIN,(255,0,0),[fud_x,fud_y,10,10])

def eat(): #Function that checks if the snake has eaten the food
	global fud_x,fud_y
	if snake_x+10>=fud_x and snake_x<=fud_x+10:
		if snake_y<=fud_y+10 and snake_y+10 >=fud_y:
			fud_x,fud_y=random.randint(0,W-10),random.randint(0,H-10)
		else:
			snake_body.pop(0)
	else:
		snake_body.pop(0)


def self_hit():# Function that checks if the snake has eaten itself
	if (snake_x,snake_y) in snake_body[:len(snake_body)-1]:
		return True
	else:
		return False


RUN=True
clock=pygame.time.Clock() #Setting a pygame clock to control the speed of the while loop



#GAMELOOP
while RUN:
	clock.tick(30)
	WIN.fill((0,0,0))#Filling the screen with a black (0,0,0) color everytime the loop runs

	for event in pygame.event.get():# Cheching for the different types of events occuring
		if event.type==pygame.QUIT:
			RUN=False

		if event.type==pygame.KEYDOWN:#Checking for a keyboard press
			if event.key==pygame.K_UP:#Checking the key pressed was an UP arrow key
				if not(del_y==10):#CHecking if the body wasn't moving downward previously
					del_y=-10
					del_x=0
			elif event.key==pygame.K_DOWN:#Checking the key pressed was a DOWN arrow key
				if not (del_y==-10):
					del_y=10
					del_x=0
			elif event.key==pygame.K_LEFT:#Checking the key pressed was a LEFT arrow key
				if not (del_x==10):
					del_y=0
					del_x=-10
			elif event.key==pygame.K_RIGHT:#Checking the key pressed was a RIGHT arrow key
				if not(del_x==-10):
					del_y=0
					del_x=10


	snake_move()
	eat()
	draw_snake()
	draw_fud()
	if self_hit():
		RUN=False # Quitting the loop as the snake has eaten itself by setting RUN as False

	pygame.display.update()# Updating the changes made to the game window


pygame.quit()#Quiting the pygame module(Optional but a good practice)






	



