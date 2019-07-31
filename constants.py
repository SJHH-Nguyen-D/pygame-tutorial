# Load Sprites
import pygame
import os

SPRITE_DIR = "/home/dennis/Desktop/Link to datascience_job_portfolio/pygame-tutorial/sprites"

WALK_RIGHT = [
	pygame.image.load(os.path.join(SPRITE_DIR, "R1.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "R2.png")),
	pygame.image.load(os.path.join(SPRITE_DIR, "R3.png")),
	pygame.image.load(os.path.join(SPRITE_DIR, "R4.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "R5.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "R6.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "R7.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "R8.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "R9.png"))
	]
WALK_LEFT = [
	pygame.image.load(os.path.join(SPRITE_DIR, "L1.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "L2.png")),
	pygame.image.load(os.path.join(SPRITE_DIR, "L3.png")),
	pygame.image.load(os.path.join(SPRITE_DIR, "L4.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "L5.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "L6.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "L7.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "L8.png")), 
	pygame.image.load(os.path.join(SPRITE_DIR, "L9.png"))
	]

BG = pygame.image.load(os.path.join(SPRITE_DIR, "bg.jpg"))
CHAR = pygame.image.load(os.path.join(SPRITE_DIR, "standing.png"))
CLOCK = pygame.time.Clock()