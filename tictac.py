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
boardFull = False

def mark_board(self, xo):
		if self.text is not "":
			return False
		elif xo < 0:
			self.text = "X"
			return True
		else: 
			self.text = "O"
			return True

gameboard = []
for row in range(3):
	for col in range(3):
		gameboard.append(Button(mark_board, (col*SCREEN_WIDTH//3,row*SCREEN_WIDTH//3), SCREEN_WIDTH//3, SCREEN_HEIGHT//3, color=(0,0,0), border_thickness=10))


while running:


	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

		elif event.type == QUIT:
			running = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			for sqr in gameboard:
				if sqr.isClicked(pygame.mouse.get_pos()):
					if sqr.action(sqr, xo):
						xo *= -1

	screen.fill((70, 70, 90))

	for sqr in gameboard:
		sqr.draw(screen)


	pygame.display.flip()

	for row in range(3):
		for col in range(3):
			print(gameboard[row*3 + col].text, end="\t")
		print("")

