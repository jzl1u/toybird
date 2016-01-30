import os
import sys
import math
import time
import pygame

current_path = os.getcwd()
sys.path.insert(0, os.path.join(current_path, "../pymunk-4.0.0"))
import pymunk as pm
#from characters import Bird
#from level import level

pygame.init()
screen = pygame.display.set_mode((1200,650))
redbird = pygame.image.load(
	"../resources/images/red-bird3.png").convert_alpha()
background2 = pygame.image.load(
	"../resources/images/background3.png").convert_alpha()
sling_image = pygame.image.load(
	"../resources/images/sling-3.png").convert_alpha()
full_sprite = pygame.image.load(
	"../resources/images/full-sprite.png").convert_alpha()


rect = pygame.Rect(181,1050,50,50)
cropped = full_sprite.subsurface(rect).copy()
pig_image = pygame.transform.scale(cropped,(30, 30))
running = True
clock = pygame.time.Clock()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	x_mouse, y_mouse = pygame.mouse.get_pos()
	
	screen.fill((130, 200, 100))
	screen.blit(background2, (0, 0))
	rect = pygame.Rect(50, 0, 40, 220)
	screen.blit(sling_image,(138,470), rect)
	pygame.display.update()
	pygame.display.set_caption("fps: "+ str(clock.get_fps()))