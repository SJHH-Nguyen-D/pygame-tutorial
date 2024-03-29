import pygame
from constants import *


# a pygame always initializes with pygame.init()
pygame.init()

# create a window with which the game will happen in with width and height of window
screen_width = 500
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First Game")

class Player(object):
	""" player class """
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.velocity = 5 # how fast our character moves
		self.is_jump = False
		self.jump_count = 10
		self.left = False
		self.right = False
		self.walk_count = 0
		self.standing = True

	def draw(self, win):
		# 27 frames = 3*9 char images
		if self.walk_count + 1 >=27:
			self.walk_count = 0

		# Drawing our character during movement
		if not self.standing:
			if self.left:
				win.blit(WALK_LEFT[self.walk_count//3], (self.x, self.y))
				self.walk_count += 1
			elif self.right:
				win.blit(WALK_RIGHT[self.walk_count//3], (self.x, self.y))
				self.walk_count += 1
			else:
				if self.right:
					win.blit(WALK_RIGHT[0], (self.x, self.y))
				elif self.left:
					win.blit(WALK_LEFT[0], (self.x, self.y))
				else:
					win.blit(CHAR, (self.x, self.y))

class Enemy(Player):
	""" enemy subclass """
	
	def __init__(self,  x, y, width, height, end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x, self.end]
		self.walk_count = 0
		self.velocity = 3

	def draw(self, win):
		self.move()
		# 33 frames because 11 enemy images * 3 instead of the the 9 images for character
		if self.walk_count + 1 >=33:
			self.walk_count = 0

		# move right
		if self.velocity > 0:
			win.blit(WALK_RIGHT_ENEMY[self.walk_count//3], (self.x, self.y))
			self.walk_count += 1
		# move left
		else:
			win.blit(WALK_LEFT_ENEMY[self.walk_count//3], (self.x, self.y))
			self.walk_count += 1
		

	def move(self):
		if self.velocity > 0:
			if self.x + self.velocity < self.path[1]:
				self.x += self.velocity
			else:
				self.velocity *= self.velocity
				self.walk_count = 0
		else:
			if self.x - self.velocity > self.path[0]:
				self.x += self.velocity
			else:
				self.velocity *= self.velocity
				self.walk_count = 0


class Projectile(object):
	""" projectile class """
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.velocity = 8*facing

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y,), self.radius)


def redraw_game_window():
	""" draw window and character sprite """
	global walk_count
	# fill background with an image with 'background lit', followed by its position
	win.blit(BG, (0, 0))
	player.draw(win)
	goblin.draw(win)
	for bullet in bullets:
		bullet.draw(win)

	pygame.display.update()


# main loop for which the game will work through
player = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, end=450)
bullets = list()
run = True
while run:
	# checks for collision in the main-loop
	# set the frame rate of the game to 27 FPS
	CLOCK.tick(27)

	# events are anything that would be inputs from the user
	# gets a list of events that happened through the items in this list
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# handling of bullets
	for bullet in bullets:
		if bullet.x < 500 and bullet.x > 0:
			bullet.x += bullet.velocity
		else:
			bullets.pop(bullets.index(bullet))

	# create a list of keys that can be pressed for the game
	# coordinates from the game start in the top left corner of the window (0,0)
	# top right of the screen would be (500, 500)
	# bottom corners of the screen are not actually negative but they are considered positive.
	keys = pygame.key.get_pressed()

	if keys[pygame.K_SPACE]:
		if player.left:
			facing = -1
		else:
			facing = 1
		if len(bullets) < 5:
			# create the bullet object first before we can start shooting them
			bullets.append(
				Projectile(
					round(player.x + player.width//2), 
					round(player.y + player.height//2), 
					6, 
					(0, 0, 0), 
					facing)
				)
	
	# WALKING
	# and if our character is moving left, we have to make sure that our character's position is 
	# greater than 0, otherwise we would be moving off the screen
	if keys[pygame.K_a] and player.x > player.velocity:
		player.x -= player.velocity
		player.right = False
		player.left = True
		player.standing = False
	elif keys[pygame.K_d] and player.x < screen_width - player.width - player.velocity:
		player.x += player.velocity
		player.right = True
		player.left = False
		player.standing = False
	else:
		player.standing = True
		player.walk_count = 0

	# JUMPING
	# no jumping in mid air or changing your trajectory during the jump
	if not(player.is_jump):
		if keys[pygame.K_w]:
			player.is_jump = True
			player.right = False
			player.left = False
			player.walk_count = 0

	# actually jumping
	else:
		# allow left and right during jump
		# on the up stroke of our jump
		if player.jump_count >= -10:
			neg = 1
			# on the down stroke of our jump
			if player.jump_count < 0:
				neg = -1
			# move the character up by a certain number of pixels
			player.y -= (player.jump_count **2) * 0.5 * neg
			player.jump_count -= 1
		else:
			player.is_jump = False
			player.jump_count = 10

	redraw_game_window()

# quit the window
pygame.display.quit()
# a pygame always ends with pygame.quit()
pygame.quit()
