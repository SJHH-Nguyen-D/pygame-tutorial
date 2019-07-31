# Load Sprites
import pygame
import os

CHAR_SPRITE_DIR = os.path.join(os.getcwd(), "char_sprites")
ENEMY_SPRITE_DIR = os.path.join(os.getcwd(), "enemy_sprites")
MISC_SPRITE_DIR = os.path.join(os.getcwd(), "misc_sprites")

# sprites for character motion and states
WALK_RIGHT = [
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "R1.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "R2.png")),
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "R3.png")),
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "R4.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "R5.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "R6.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "R7.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "R8.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "R9.png"))
	]

WALK_LEFT = [
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "L1.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "L2.png")),
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "L3.png")),
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "L4.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "L5.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "L6.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "L7.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "L8.png")), 
	pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "L9.png"))
	]

CHAR = pygame.image.load(os.path.join(CHAR_SPRITE_DIR, "standing.png"))

# sprites for enemy
WALK_RIGHT_ENEMY = [
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R1E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R2E.png")),
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R3E.png")),
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R4E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R5E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R6E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R7E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R8E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R9E.png")),
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R10E.png")),
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "R11E.png"))
	]

WALK_LEFT_ENEMY = [
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L1E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L2E.png")),
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L3E.png")),
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L4E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L5E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L6E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L7E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L8E.png")), 
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L9E.png")),
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L10E.png")),
	pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "L11E.png"))
	]

CHAR = pygame.image.load(os.path.join(ENEMY_SPRITE_DIR, "standingE.png"))

BG = pygame.image.load(os.path.join(MISC_SPRITE_DIR, "bg.jpg"))

CLOCK = pygame.time.Clock()