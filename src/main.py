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
buttons = pygame.image.load(
	"../resources/images/selected-buttons.png").convert_alpha()
stars = pygame.image.load(
	"../resources/images/stars-edited.png").convert_alpha()
rect = pygame.Rect(0,0,200,200)
star1 =  stars.subsurface(rect).copy()
rect = pygame.Rect(204, 0, 200, 200)
star2 = stars.subsurface(rect).copy()
rect = pygame.Rect(426, 0, 200, 200)
star3 = stars.subsurface(rect).copy()
rect = pygame.Rect(164, 10, 60, 60)
pause_b = buttons.subsurface(rect).copy()
rect = pygame.Rect(24, 4, 100, 100)
replay_b = buttons.subsurface(rect).copy()
rect = pygame.Rect(142, 365, 130, 100)
next_b = buttons.subsurface(rect).copy()
rect = pygame.Rect(18, 212, 100, 100)
play_b = buttons.subsurface(rect).copy()
rect = pygame.Rect(181,1050,50,50)
cropped = full_sprite.subsurface(rect).copy()
pig_image = pygame.transform.scale(cropped,(30, 30))
running = True
clock = pygame.time.Clock()
game_state = 0

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	x_mouse, y_mouse = pygame.mouse.get_pos()
	if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
		if (x_mouse < 60 and y_mouse < 155 and y_mouse > 90):
			game_state = 1
		
	screen.fill((130, 200, 100))
	screen.blit(background2, (0, 0))
	rect = pygame.Rect(50, 0, 40, 220)
	screen.blit(sling_image,(138,470), rect)
	if game_state == 1:
		screen.blit(play_b, (500, 200))
		screen.blit(replay_b, (500, 300))
	pygame.display.update()
	pygame.display.set_caption(str(x_mouse)+str(y_mouse)+str(game_state)+"fps: "+ str(clock.get_fps()))