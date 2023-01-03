import pygame
from enum import Enum
from config import DINO_X, DINO_Y, FPS, CACTUS_Y

class DinoState(Enum):
    RUN = 'RUN'
    JUMP = 'JUMP'


class Dino:
	runAnimationIndex = 0
	currentRunSpriteIndex = 0
	jumpPower = 10
	curJumpPower = jumpPower
	hitbox = None
	image = None
	state = DinoState.RUN
	color = 'default'
	sprites = {
		DinoState.RUN: [],
		DinoState.JUMP: [],
	}

	def __init__(self, color='default', name=None):
		self.color = color
		self.loadSprites()
		self.image = self.sprites[DinoState.RUN][0]
		self.hitbox = pygame.Rect(
			DINO_X,
			DINO_Y,
			self.sprites[DinoState.RUN][0].get_width(),
			self.sprites[DinoState.RUN][0].get_height()
		)

		if name is not None:
			self.name = name

	def loadSprites(self):
		# load sprites
		run1Sprite = pygame.image.load(f"sprites/dino/{self.color}_run1.png").convert()
		run2Sprite = pygame.image.load(f"sprites/dino/{self.color}_run2.png").convert()
		jumpSprite = pygame.image.load(f"sprites/dino/{self.color}_jump.png").convert()

		# filter black pixels
		run1Sprite.set_colorkey((0, 0, 0))
		run2Sprite.set_colorkey((0, 0, 0))
		jumpSprite.set_colorkey((0, 0, 0))

		self.sprites[DinoState.RUN].append(run1Sprite)
		self.sprites[DinoState.RUN].append(run2Sprite)
		self.sprites[DinoState.JUMP].append(jumpSprite)

	def run(self):
		self.runAnimationIndex += 1

		if self.runAnimationIndex == FPS // 6:
			self.runAnimationIndex = 0

			if self.currentRunSpriteIndex == 0:
				self.currentRunSpriteIndex = 1
			else:
				self.currentRunSpriteIndex = 0

		self.image = self.sprites[DinoState.RUN][self.currentRunSpriteIndex]

	def jump(self, gameSpeed):
		if self.state == DinoState.JUMP:
			self.hitbox.y -= self.curJumpPower * (2 * (gameSpeed / 8))
			self.curJumpPower -= 0.5 * (gameSpeed / 8)

			# reset state after dina landed
			if self.hitbox.y >= DINO_Y:
				self.hitbox.y = DINO_Y
				self.state = DinoState.RUN
				self.curJumpPower = self.jumpPower

		else:
			self.state = DinoState.JUMP
			self.image = self.sprites[DinoState.JUMP][0]

	def update(self, gameSpeed):
		if self.state == DinoState.RUN:
			self.run()
		elif self.state == DinoState.JUMP:
			self.jump(gameSpeed)

	def draw(self, screen, withHitbox = False):
		screen.blit(self.image, self.hitbox)

		if withHitbox is True:
			pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)