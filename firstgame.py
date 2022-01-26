import pygame
import random

pygame.init()
W=500
H=500

WIN=pygame.display.set_mode((W,H))
pygame.display.set_caption("SNAKE GAME")

snake_x=W//2
snake_y=H//2
del_x=0
del_y=0
fud_x,fud_y=random.randint(0,W),random.randint(0,H)
snake_body=[(snake_x,snake_y)]


def draw_snake():
	for body in snake_body:
		pygame.draw.rect(WIN,(255,255,255),[body[0],body[1],10,10])

def snake_move():
	global snake_x,snake_y
	snake_y=(snake_y+del_y)%H
	snake_x=(snake_x+del_x)%W
	snake_body.append((snake_x,snake_y))

def draw_fud():
	pygame.draw.rect(WIN,(255,0,0),[fud_x,fud_y,10,10])

def eat():
	global fud_x,fud_y
	if snake_x+10>=fud_x and snake_x<=fud_x+10:
		if snake_y<=fud_y+10 and snake_y+10 >=fud_y:
			fud_x,fud_y=random.randint(0,W-10),random.randint(0,H-10)
		else:
			snake_body.pop(0)
	else:
		snake_body.pop(0)


def self_hit():
	if (snake_x,snake_y) in snake_body[:len(snake_body)-1]:
		return True
	else:
		return False


RUN=True
clock=pygame.time.Clock()
while RUN:
	clock.tick(30)
	WIN.fill((0,0,0))

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			RUN=False

		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_UP:
				if not(del_y==10):
					del_y=-10
					del_x=0
			elif event.key==pygame.K_DOWN:
				if not (del_y==-10):
					del_y=10
					del_x=0
			elif event.key==pygame.K_LEFT:
				if not (del_x==10):
					del_y=0
					del_x=-10
			elif event.key==pygame.K_RIGHT:
				if not(del_x==-10):
					del_y=0
					del_x=10


	snake_move()
	eat()
	draw_snake()
	draw_fud()
	if self_hit():
		RUN=False

	pygame.display.update()


pygame.quit()






	



