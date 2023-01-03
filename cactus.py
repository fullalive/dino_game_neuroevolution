import pygame
import random
from config import WIDTH, CACTUS_Y

class Cactus():
	availableTypes = ["1", "2", "3", "4", "5", "6"]
	cactusType = None
	image = None
	hitbox = None
	isActive = True

	def __init__(self, x):
		self.loadImage()
		self.hitbox.x = x
		self.hitbox.y = CACTUS_Y - self.hitbox.height

	def loadImage(self):
		if self.cactusType is None:
			self.randomizeCactusType()

		self.image = pygame.image.load(f'sprites/cactus/{self.cactusType}.png').convert()
		self.image.set_colorkey((0, 0, 0))
		self.hitbox = self.image.get_rect()

	def randomizeCactusType(self):
		self.cactusType = random.choice(self.availableTypes)
	
	def update(self, gameSpeed):
		self.hitbox.x -= gameSpeed

		# if the cactus has gone off the screen, we delete it
		if self.hitbox.x < -self.hitbox.width:
			self.isActive = False
	
	def draw(self, screen, withHitbox = False):
		screen.blit(self.image, self.hitbox)

		if withHitbox is True:
			pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)		
	
	# create initializeCactusList static method
	@staticmethod
	def initializeCactusList():
		return [
			Cactus(WIDTH + 300 / random.uniform(0.8, 3)),
			Cactus(WIDTH * 2 + 200 / random.uniform(0.8, 3)),
			Cactus(WIDTH * 3 + 400 / random.uniform(0.8, 3)),
		]