import pygame

pygame.init()
width = 640
height = 480

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)

screen = pygame.display.set_mode((width, height))

running = True
clock = pygame.time.Clock()
dt = clock.tick()

class Ball:
	def __init__(self):
		self.x = 50
		self.y = 50
		self.speedx = 1
		self.speedy = 1
		self.radius = 20

	def updatePosition(self):
		if self.x >= width-self.radius:
			self.speedx = abs(self.speedx) *-1
		elif self.x <= self.radius:
			self.speedx = abs(self.speedx)
		if self.y >= height-self.radius:
			self.speedy = abs(self.speedy) *-1
		elif self.y <= self.radius:
			self.speedy = abs(self.speedy)
		self.x += self.speedx * dt
		self.y += self.speedy * dt

	def getPosition(self):
		return (self.x,self.y)

	def draw(self):
		pygame.draw.circle(screen, GREEN, (self.x,self.y), self.radius)


class Paddle:
	def __init__(self):
		self.x = 50
		self.y = 50

	def moveDown(self):
		self.y += 1

	def moveUp(self):
		self.y -= 1

	def getPosition(self):
		return (self.x,self.y)

b = Ball()
p = Paddle()
upKeyPressed = False
downKeyPressed = False

#def getPos():
#    pos = pygame.mouse.get_pos()
#    return (pos)

#def drawCircle():
#    pos= b.getPosition()
#    pygame.draw.circle(screen, BLUE, pos, 20)

#def drawPaddle():
#	x = p.x
#	y = p.y
#	pygame.draw.rect(screen, BLUE, [x,y,10,50])

while running:
        ev = pygame.event.get()
        dt = int(clock.tick(30) * .2)

        '''for event in ev:

            if event.type == pygame.KEYDOWN:

            	up = True

            if event.type == pygame.KEYUP:
            	up = False

            if event.type == pygame.QUIT:
                running = False

        if up:
        	p.moveDown()'''

        screen.fill(BLUE)

        b.updatePosition()
        b.draw()
        pygame.display.update()






