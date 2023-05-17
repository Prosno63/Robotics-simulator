import pygame
import pymunk
import math
from random import randint

class Ball():
	def __init__(self, x, y, size):
		self.size=size
		mass = self.size**2               # mass given for each object.
		self.color=(randint(0, 255), randint(0, 255), randint(0, 255))
		angle=randint(0, 359)             # random angle
		coeff=10000/mass                  # we assume that each ball regardless of it's size has the same momentum initially, which is 10000
		self.body=pymunk.Body(mass)      
		self.body.position=(x, y)
		self.body.velocity=(coeff*math.cos(angle*math.pi/180), coeff*math.sin(angle*math.pi/180))
		self.shape=pymunk.Circle(self.body, self.size)
		self.shape.elasticity = 1         # elasticity determines how bouncy the ball is, Value 1 means a perfect bounce 
		self.shape.density = 1            # If the relative density is exactly 1 then the densities are equal; that is, equal volumes of the two substances have the same mass.
		space.add(self.body, self.shape)
    
    #function to visualize the objects
	def draw(self):
		x=int(self.body.position.x)
		y=int(self.body.position.y)
		pygame.draw.circle(wn, self.color, (x,y), self.size)

def create_segment(pos1, pos2):           # pos1 and Pos2 are starting and ending position of a segment
	segment_body = pymunk.Body(body_type = pymunk.Body.STATIC)
	segment_shape=pymunk.Segment(segment_body, pos1, pos2, 5)  # Distance from wind border
	segment_shape.elasticity = 1
	space.add(segment_body, segment_shape)

pygame.init()
wn=pygame.display.set_mode((800, 800))
clock=pygame.time.Clock()
space=pymunk.Space()

FPS =   45                               # Frames Per Second, is the number of frames shown per unit of time (50 distinct still images)
WHITE = (255, 255, 255)
BLACK = (0,0,0)                           # Window colour
balls=[Ball(randint(0, 800), randint(0, 800), randint(10, 20)) for i in range(25)]
pos_tl=(0,0)
pos_tr=(800, 0)
pos_bl=(0, 800)
pos_br=(800, 800)
segment1=create_segment(pos_tl, pos_tr)
segment2=create_segment(pos_tr, pos_br)
segment3=create_segment(pos_br, pos_bl)
segment4=create_segment(pos_bl, pos_tl)

running=True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

	wn.fill(BLACK)
	[ball.draw() for ball in balls]
	pygame.draw.line(wn, WHITE, pos_tl, pos_tr, 5)
	pygame.draw.line(wn, WHITE, pos_tr, pos_br, 5)
	pygame.draw.line(wn, WHITE, pos_br, pos_bl, 5) 
	pygame.draw.line(wn, WHITE, pos_bl, pos_tl, 5)  

	pygame.display.flip()
	clock.tick(FPS)     # Tick is just a measure of time in PyGame. clock.tick(50) means that for every second at most 50 frames should pass.
	space.step(1/FPS)   # is the amount of time should pass between each frame.

pygame.quit()