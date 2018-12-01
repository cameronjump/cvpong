import pygame
import random

pygame.init()
width = 640
height = 480

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
ORANGE =     (255, 165,   0)
RED =       (255,   0,   0)

screen = pygame.display.set_mode((width, height))

running = True
clock = pygame.time.Clock()
dt = clock.tick()
font = pygame.font.SysFont("comicsansms", 72)
scoreA = 0
scoreB = 0

class Ball:
	def __init__(self):
		self.x = int(width/2)
		self.y = int(height/2)
		self.speedx = int(random.uniform(1,5)) * random.choice([-1, 1])
		self.speedy = int(random.uniform(1,5)) * random.choice([-1, 1])
		self.radius = 20

	def updatePosition(self):
		#if self.x >= width-self.radius:
		#	self.speedx = abs(self.speedx) *-1
		#elif self.x <= self.radius:
		#	self.speedx = abs(self.speedx)
		if self.y >= height-self.radius:
			self.speedy = abs(self.speedy) *-1
		elif self.y <= self.radius:
			self.speedy = abs(self.speedy)
		self.x += self.speedx * dt
		self.y += self.speedy * dt

	def isScore(self):
		if self.x >= width-self.radius:
			return (True, 'A')
		elif self.x <= self.radius:
			return (True, 'B')
		return (False , None)

	def getPosition(self):
		return (self.x,self.y)

	def draw(self):
		pygame.draw.circle(screen, ORANGE, (self.x,self.y), self.radius)

def drawField():
	pygame.draw.rect(screen,WHITE, [int(width/2),0,2,height])
	font = pygame.font.SysFont("comicsansms", 72)
	textA = font.render(str(scoreA), True, (0, 128, 0))
	textB = font.render(str(scoreB), True, (0, 128, 0))
	screen.blit(textA,(10, 10))
	screen.blit(textB,(width-textA.get_width()-10, 10))





b = Ball()
#p = Paddle()
#upKeyPressed = False
#downKeyPressed = False

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
        dt = int(clock.tick(30) * .1)

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
        drawField()

        b.updatePosition()
        b.draw()

        wasScore, score = b.isScore()
        if wasScore:
        	b = Ball()
        	if score == 'A':
        		scoreA += 1
        	else:
        		scoreB += 1

        pygame.display.update()






