import pygame

pygame.init()
width = 1200
height = 600

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)

screen = pygame.display.set_mode((width, height))

running = True

class Ball:
	def __init__(self):
		self.x = 50
		self.y = 50

	def updatePosition(self):
		self.x += 1
		self.y += 1

	def getPosition(self):
		return (self.x,self.y)

b = Ball()

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawCircle():
    pos= b.getPosition()
    b.updatePosition()
    pygame.draw.circle(screen, BLUE, pos, 20)

while running:
        ev = pygame.event.get()
        screen.fill(GREEN)

        for event in ev:

            if event.type == pygame.KEYUP:
            	drawCircle()
            	b.updatePosition()
            	pygame.display.update()

            if event.type == pygame.QUIT:
                running = False'''


