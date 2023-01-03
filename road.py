import pygame
from config import ROAD_Y

class Road:
	image = None
	roadImageRect = None
	chunks = []

	def __init__(self):
		self.roadImage = pygame.image.load('sprites/road.png').convert()
		self.roadImage.set_colorkey((0, 0, 0))
		self.roadImageRect = self.roadImage.get_rect()
		self.chunks = [
			{'image': self.roadImage, 'x': 0, 'y': ROAD_Y},
			{'image': self.roadImage, 'x': self.roadImageRect.width, 'y': ROAD_Y},
			{'image': self.roadImage, 'x': self.roadImageRect.width * 2, 'y': ROAD_Y},
		]

	def draw(self, screen, gameSpeed):
		if (self.chunks[0]['x'] < -self.roadImageRect.width):
			self.chunks[0]['x'] = self.chunks[2]['x'] + self.roadImageRect.width
			self.chunks[0], self.chunks[1], self.chunks[2] = self.chunks[1], self.chunks[2], self.chunks[0]

		for roadChunk in self.chunks:
			roadChunk['x'] -= gameSpeed
			screen.blit(roadChunk['image'], (roadChunk['x'], roadChunk['y']))