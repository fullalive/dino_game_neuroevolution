import pygame
import random
import math
from cactus import Cactus
from road import Road
from dino import Dino, DinoState
from config import WIDTH, HEIGHT, FPS, BGColor, SCORE_COLOR

class Game():
	# Fonts
	font = None
	scoreFont = None
	dnameFont = None
	headingFont = None

	# Game parameters
	generation = 0
	showHitboxes = False
	score = 0
	scoreSpeedup = 200
	gameSpeed = 18.0
	skins = ["default", "aqua", "black", "bloody", "cobalt", "gold", "insta",
			"lime", "magenta", "magma", "navy", "neon", "orange", "pinky",
			"purple", "rgb", "silver", "subaru", "sunny", "toxic"]
	names = ["Флафи", "Фалафель", "Ведьмак", "Лютик", "Пучеглазик", "Слайм", "Шустрый", "Следопыт",
			"Малыш", "Субарик", "Т-Рекс", "Птенец", "Рядовой", "Опытный", "Ветеран", "Геймер",
			"Самурай", "Странник"]
	generation = 0

	def initializeFonts(self):
		self.font = pygame.font.SysFont("Roboto Condensed", 30)
		self.scoreFont = pygame.font.SysFont("Roboto Condensed", 40)
		self.dnameFont = pygame.font.SysFont("Roboto Condensed", 30)
		self.headingFont = pygame.font.SysFont("Roboto Condensed", 70)

	def updateAndDrawScore(self, screen):
		self.score += 0.5 * (self.gameSpeed / 8)

		if self.score > self.scoreSpeedup:
			self.scoreSpeedup += 100 * (self.gameSpeed / 4)
			self.gameSpeed += 1

		scoreLabel = self.scoreFont.render('Score: ' + str(math.floor(self.score)), True, SCORE_COLOR)
		scoreLabelRect = scoreLabel.get_rect()
		scoreLabelRect.y = 50
		scoreLabelRect.left = WIDTH - 220


		screen.blit(scoreLabel, scoreLabelRect)

	def drawSpeed(self, screen):
		speedLabel = self.scoreFont.render('Speed: ' + str(self.gameSpeed), True, SCORE_COLOR)
		labelRect = speedLabel.get_rect()
		labelRect.center = (WIDTH / 2, 50 + labelRect.height / 2)
		screen.blit(speedLabel, labelRect)


	def runGame(self):
		pygame.init()
		screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption('Dino Game')
		clock = pygame.time.Clock()

		self.initializeFonts()

		# Game objects
		road = Road()
		enemies = Cactus.initializeCactusList()
		dino = Dino()

		# Game cycle
		running = True
		while True:
			screen.fill(BGColor)

			for event in pygame.event.get():
				# check for closing window
				if event.type == pygame.QUIT:
					running = False
					pygame.quit()
					return

			# keep showing game screen with score, but skip any updates
			if running is False:
				continue

			# render road
			road.draw(screen, self.gameSpeed)

			# render dino
			dino.update(self.gameSpeed)
			dino.draw(screen, self.showHitboxes)

			# add new enemy after every success jump
			if len(enemies) < 3:
				enemies.append(Cactus(enemies[len(enemies) - 1].hitbox.x + WIDTH / random.uniform(0.8, 3)))

			enemyIdsToRemove = []

			for i, enemy in enumerate(enemies):
				enemy.update(self.gameSpeed)
				enemy.draw(screen, self.showHitboxes)

				if not enemy.isActive:
					enemyIdsToRemove.append(i)
					continue

				# stop game if collide
				if dino.hitbox.colliderect(enemy.hitbox):
					running = False

			# remove all inactive enemies
			for i in enemyIdsToRemove:
				enemies.pop(i)

			# controls
			userInput = pygame.key.get_pressed()
			if userInput[pygame.K_SPACE] and not dino.state == DinoState.JUMP:
				dino.jump(self.gameSpeed)

			# score and its label
			self.updateAndDrawScore(screen)

			# draw current speed
			self.drawSpeed(screen)

			pygame.display.flip()
			clock.tick(FPS)
