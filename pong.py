import pygame
import random
from threading import Thread
import os
import time
import cv2
import numpy as np
import os

blueLower = np.array([100, 67, 0], dtype = "uint8")
blueUpper = np.array([255, 128, 50], dtype = "uint8")


camera = cv2.VideoCapture(0)

pygame.init()
width = 1000#1800
height = 500#980

WHITE =     (255, 255, 255)
BLACK =      (  0,   0, 0)
ORANGE =     (255, 165,   0)
RED =       (255,   0,   0)

screen = pygame.display.set_mode((width, height))#,pygame.FULLSCREEN)
pygame.display.set_caption('cvpong')

running = True
clock = pygame.time.Clock()
dt = clock.tick()
font = pygame.font.SysFont("comicsansms", 72)
scoreA = 0
scoreB = 0

x1, y1, x2, y2 = .1, .5, .5, .9

class Ball:
	def __init__(self):
		self.x = int(width/2)
		self.y = int(height/2)
		self.speedx = random.uniform(1,5) * random.choice([-1, 1])
		self.speedy = random.uniform(1,5) * random.choice([-1, 1])
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
		self.x += int(self.speedx * dt)
		self.y += int(self.speedy * dt)

	def reverse(self):
		self.speedx *= -1

	def getRect(self):
		return pygame.Rect(self.x,self.y,self.radius,self.radius)

	def isScore(self):
		if self.x >= width+2*self.radius:
			return (True, 'A')
		elif self.x <= -2*self.radius:
			return (True, 'B')
		return (False , None)

	def draw(self):
		pygame.draw.circle(screen, ORANGE, (self.x,self.y), self.radius)

class Paddle:
	def __init__(self):
		self.x = int(20)
		self.y = int(height/2)
		self.width = int(width/40)
		self.height = height/2#int(height/6)

	def updatePosition(self, x, y):
		self.x = x*width
		self.y = y*height

	def getRect(self):
		return pygame.Rect(self.x,self.y,self.width,self.height)


	def draw(self):
		pygame.draw.rect(screen, ORANGE, self.getRect())


def drawField():
	pygame.draw.rect(screen,WHITE, [int(width/2),0,2,height])
	font = pygame.font.SysFont("comicsansms", 72)
	textA = font.render(str(scoreA), True, WHITE)
	textB = font.render(str(scoreB), True, WHITE)
	screen.blit(textA,(10, 10))
	screen.blit(textB,(width-textA.get_width()-10, 10))





b = Ball()
p1 = Paddle()
p2 = Paddle()
#p = Paddle()
#upKeyPressed = False
#downKeyPressed = False

#def getPos():
#    pos = pygame.mouse.get_pos()
#    return (pos)

#def drawCircle():
#    pos= b.getPosition()
#    pygame.draw.circle(screen, BLACK, pos, 20)

#def drawPaddle():
#	x = p.x
#	y = p.y
#	pygame.draw.rect(screen, BLACK, [x,y,10,50])

'''def cv():
	global running, x1, y1, x2, y2 
	while running:
	    # grab the current frame
	    (grabbed, frame) = camera.read()

	    # check to see if we have reached the end of the
	    # video
	    if not grabbed:
	        break

	    # determine which pixels fall within the blue boundaries
	    # and then blur the binary image
	    blue = cv2.inRange(frame, blueLower, blueUpper)
	    blue = cv2.GaussianBlur(blue, (3, 3), 0)

	    # find contours in the image
	    (_, cnts, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL,
	        cv2.CHAIN_APPROX_SIMPLE)

	    # check to see if any contours were found
	    if len(cnts) > 0:
	        # sort the contours and find the largest one -- we
	        # will assume this contour correspondes to the area
	        # of my phone
	        cnt1, cnt2 = None, None
	        try:
	        	cnt1 = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
	        	cnt2 = sorted(cnts, key = cv2.contourArea, reverse = True)[1]
	        except:
	        	continue

	        # compute the (rotated) bounding box around then
	        # contour and then draw it      
	        rect1 = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt1)))

	        # find center of first rec
	        coor1 = (cv2.boxPoints(cv2.minAreaRect(cnt1)))
	        # x and y coor of points
	        x11 = coor1[(0, 0)]
	        y11 = coor1[(0, 1)]
	        x12 = coor1[(1, 0)]
	        y12 = coor1[(1, 1)]
	        x13 = coor1[(2, 0)]
	        y13 = coor1[(2, 1)]
	        x14 = coor1[(3, 0)]
	        y14 = coor1[(3, 1)]

	        # Average values (center)
	        center1 = ((x11+x12+x13+x14)/(640*4), (y11+y12+y13+y14)/(480*4))
	        x1 = center1[0]
	        y1 = center1[1]

	        # find center of second rec
	        rect2 = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt2)))
	        coor2 = (cv2.boxPoints(cv2.minAreaRect(cnt2)))

	        # x and y coor of second rec
	        x21 = coor2[(0, 0)]
	        y21 = coor2[(0, 1)]
	        x22 = coor2[(1, 0)]
	        y22 = coor2[(1, 1)]
	        x23 = coor2[(2, 0)]
	        y23 = coor2[(2, 1)]
	        x24 = coor2[(3, 0)]
	        y24 = coor2[(3, 1)]

	        # Average values (center)
	        center2 = ((x21 + x22 + x23 + x24) / (640*4), (y21 + y22 + y23 + y24) / (480*4))
	        x2 = center2[0]
	        y2 = center2[1]

	        cv2.drawContours(frame, [rect1], -1, (0, 255, 0), 2)
	        rect2 = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt2)))
	        cv2.drawContours(frame, [rect2], -1, (0, 255, 0), 2)


	    # show the frame and the binary image
	    cv2.imshow("Tracking", frame)
	    #cv2.imshow("Binary", blue)

	    # if your machine is fast, it may display the frames in
	    # what appears to be 'fast forward' since more than 32
	    # frames per second are being displayed -- a simple hack
	    # is just to sleep for a tiny bit in between frames;
	    # however, if your computer is slow, you probably want to
	    # comment out this line
	    time.sleep(0.025)

	    # if the 'q' key is pressed, stop the loop
	    if cv2.waitKey(1) & 0xFF == ord("q"):
	        break

thread = Thread( target=cv, args=())
thread.start()
thread.join()'''

while running:
		# grab the current frame
	    (grabbed, frame) = camera.read()

	    # check to see if we have reached the end of the
	    # video
	    if not grabbed:
	        break

	    # determine which pixels fall within the blue boundaries
	    # and then blur the binary image
	    blue = cv2.inRange(frame, blueLower, blueUpper)
	    blue = cv2.GaussianBlur(blue, (3, 3), 0)

	    # find contours in the image
	    (_, cnts, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL,
	        cv2.CHAIN_APPROX_SIMPLE)

	    # check to see if any contours were found
	    if len(cnts) > 0:
	        # sort the contours and find the largest one -- we
	        # will assume this contour correspondes to the area
	        # of my phone
	        cnt1, cnt2 = None, None
	        try:
	        	cnt1 = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
	        	cnt2 = sorted(cnts, key = cv2.contourArea, reverse = True)[1]
	        except: 
	        	continue

	        # compute the (rotated) bounding box around then
	        # contour and then draw it      
	        rect1 = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt1)))

	        # find center of first rec
	        coor1 = (cv2.boxPoints(cv2.minAreaRect(cnt1)))
	        # x and y coor of points
	        x11 = coor1[(0, 0)]
	        y11 = coor1[(0, 1)]
	        x12 = coor1[(1, 0)]
	        y12 = coor1[(1, 1)]
	        x13 = coor1[(2, 0)]
	        y13 = coor1[(2, 1)]
	        x14 = coor1[(3, 0)]
	        y14 = coor1[(3, 1)]

	        # Average values (center)
	        center1 = ((x11+x12+x13+x14)/(640*4), (y11+y12+y13+y14)/(480*4))
	        print(center1)
	        x1 = center1[0]
	        y2 = center1[1]


	        # find center of second rec
	        rect2 = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt2)))
	        coor2 = (cv2.boxPoints(cv2.minAreaRect(cnt2)))

	        # x and y coor of second rec
	        x21 = coor2[(0, 0)]
	        y21 = coor2[(0, 1)]
	        x22 = coor2[(1, 0)]
	        y22 = coor2[(1, 1)]
	        x23 = coor2[(2, 0)]
	        y23 = coor2[(2, 1)]
	        x24 = coor2[(3, 0)]
	        y24 = coor2[(3, 1)]

	        # Average values (center)
	        center2 = ((x21 + x22 + x23 + x24) / (640*4), (y21 + y22 + y23 + y24) / (480*4))
	        print(center2)
	        x2 = center2[0]
	        y2 = center2[1]

	        cv2.drawContours(frame, [rect1], -1, (0, 255, 0), 2)
	        rect2 = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt2)))
	        cv2.drawContours(frame, [rect2], -1, (0, 255, 0), 2)


	    # show the frame and the binary image
	    cv2.imshow("Tracking", frame)
	    #cv2.imshow("Binary", blue)

	    # if your machine is fast, it may display the frames in
	    # what appears to be 'fast forward' since more than 32
	    # frames per second are being displayed -- a simple hack
	    # is just to sleep for a tiny bit in between frames;
	    # however, if your computer is slow, you probably want to
	    # comment out this line
	    time.sleep(0.025)

	    # if the 'q' key is pressed, stop the loop
	    if cv2.waitKey(1) & 0xFF == ord("q"):
	        break

	    ev = pygame.event.get()
	    dt = int(clock.tick(30) * .1)

	    for event in ev:
	    	if event.type == pygame.KEYUP:
	    		if event.key == pygame.K_ESCAPE:
	    			running = False

	    screen.fill(BLACK)
	    drawField()

	    if p1.getRect().colliderect(b.getRect()):
	    	b.reverse()

	    if p2.getRect().colliderect(b.getRect()):
	    	b.reverse()

	    b.updatePosition()
	    p1.updatePosition(x1,y1)
	    p2.updatePosition(x2,y2)

	    b.draw()
	    p1.draw()
	    p2.draw()

	    wasScore, score = b.isScore()
	    if wasScore:
	    	b = Ball()
	    	if score == 'A':
	    		scoreA += 1
	    	else:
	    		scoreB += 1
	    pygame.display.update()

pygame.quit()
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()






