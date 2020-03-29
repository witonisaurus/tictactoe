import pygame

class Button():
	def __init__(self, action, loc, width, height, color=None, text=None, border_thickness=None):
		self.action = action
		self.loc = loc
		self.width = width
		self.height = height
		self.color = color if color is not None else (100, 100, 100)
		self.text = text if text is not None else ""
		self.border_thickness = border_thickness if border_thickness is not None else 0

		self.rect = pygame.Rect(self.loc[0], self.loc[1], self.width, self.height)

	def isClicked(self, mouseCoords):
		isC = True
		if mouseCoords[0] < self.loc[0] or mouseCoords[0] > (self.loc[0] + self.width):
			isC = False
		if mouseCoords[1] < self.loc[1] or mouseCoords[1] > (self.loc[1] + self.width):
			isC = False

		return isC

	def draw(self, canvas):
		pygame.draw.rect(canvas, self.color, self.rect, self.border_thickness)

		font = pygame.font.Font('freesansbold.ttf', self.height//3)
		txt = font.render(self.text, True, (0,0,0))
		txtRect = txt.get_rect()
		txtRect.center = (self.loc[0] + (self.width//2),self.loc[1] + (self.height//2))

		canvas.blit(txt, txtRect)


def main():
	pass


if __name__ == '__main__':
	main()