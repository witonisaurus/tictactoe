import pygame
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT)
from Button import Button

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
xo = -1
gameboard = [[0,0,0],[0,0,0],[0,0,0]]
winner = 'asdf'
isWinner = False
oWins = 0
xWins = 0
boardFull = False

def action(self, xo):
		if xo < 0:
			self.text = "X"
		else: 
			self.text = "O"

gameboard = []
for row in range(3):
	for col in range(3):
		gameboard.append(Button(action, (col*SCREEN_WIDTH//3,row*SCREEN_WIDTH//3), SCREEN_WIDTH//3, SCREEN_HEIGHT//3, color=(0,0,0), border_thickness=10))


while running:


	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

		elif event.type == QUIT:
			running = False

	screen.fill((70, 70, 90))


	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			for sqr in gameboard:
				if sqr.isClicked(pygame.mouse.get_pos()):
					sqr.action(sqr, xo)
					print(sqr.text)
	for sqr in gameboard:
		sqr.draw(screen)


	pygame.display.flip()

