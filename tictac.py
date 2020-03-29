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
global xo 
xo = -1
test = ""


def mark_board(self, xo):
		if self.text is not " ":
			return False
		elif xo < 0:
			self.text = "X"
			return True
		else: 
			self.text = "O"
			return True

def isGameOver(gameboard, i):
	# check dummy
	if i < 0:
		return False

	# check cols
	if gameboard[i].text is gameboard[(i+3)%9].text and gameboard[i].text is gameboard[(i+6)%9].text:
		return True
	# check rows
	else:
		i = i - i%3
		if gameboard[i].text is gameboard[i+1].text and gameboard[i].text is gameboard[i+2].text:
			return True

	# check diags
	if gameboard[0].text is gameboard[4].text and gameboard[0].text is gameboard[8].text and gameboard[0].text is not " " or gameboard[6].text is gameboard[4].text and gameboard[6].text is gameboard[2].text and gameboard[4].text is not " ":
		return True

	# draw
	flag = True

	for space in gameboard:
		if space.text is " ":
			flag = False

	if flag:
		global xo 
		xo = 0
	return flag

def reset_board():
	gameboard = []
	for row in range(3):
		for col in range(3):
			gameboard.append(Button(mark_board, (col*SCREEN_WIDTH//3,row*SCREEN_WIDTH//3), SCREEN_WIDTH//3, SCREEN_HEIGHT//3, color=(0,0,0), border_thickness=10))
	return gameboard

gameboard = reset_board()

latest_move = -1

while running:


	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

		elif event.type == QUIT:
			running = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			for i in range(len(gameboard)):
				sqr = gameboard[i]
				if sqr.isClicked(pygame.mouse.get_pos()):
					if sqr.action(sqr, xo):
						xo *= -1
						latest_move = i

	screen.fill((70, 70, 90))

	for sqr in gameboard:
		sqr.draw(screen)

	if isGameOver(gameboard, latest_move):
		latest_move = -1
		gameboard = reset_board()

		screen.fill((70, 70, 90))
		font = pygame.font.Font('freesansbold.ttf', SCREEN_HEIGHT//5)

		xo *= -1
		if xo < 0:
			txt = font.render("X WINS", True, (0,0,0))
		elif xo > 0:
			txt = font.render("O WINS", True, (0,0,0))
		else:
			txt = font.render("Draw", True, (0,0,0))
		xo = -1
		txtRect = txt.get_rect()
		txtRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

		screen.blit(txt, txtRect)
		pygame.display.flip()


		flag = True
		while flag:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					flag = False
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						running = False
						flag = False
				elif event.type == QUIT:
					running = False
					flag = False


	pygame.display.flip()

