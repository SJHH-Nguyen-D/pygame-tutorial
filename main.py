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

	def draw(self, win):
		if self.walk_count + 1 >=27:
			self.walk_count = 0

		# Drawing our character during left movement
		if self.left:
			win.blit(WALK_LEFT[self.walk_count//3], (self.x, self.y))
			self.walk_count += 1
		elif self.right:
			win.blit(WALK_RIGHT[self.walk_count//3], (self.x, self.y))
			self.walk_count += 1
		else:
			win.blit(CHAR, (self.x, self.y))
			self.walk_count += 0


def redraw_game_window():
	""" draw window and character sprite """
	global walk_count
	# fill background with an image with 'background lit', followed by its position
	win.blit(BG, (0, 0))
	player.draw(win)
	pygame.display.update()


# main loop for which the game will work through
player = Player(300, 410, 64, 64)
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

	# create a list of keys that can be pressed for the game
	# coordinates from the game start in the top left corner of the window (0,0)
	# top right of the screen would be (500, 500)
	# bottom corners of the screen are not actually negative but they are considered positive.
	keys = pygame.key.get_pressed()
	
	# WALKING
	# and if our character is moving left, we have to make sure that our character's position is 
	# greater than 0, otherwise we would be moving off the screen
	if keys[pygame.K_a] and player.x > player.velocity:
		player.x -= player.velocity
		player.right = False
		player.left = True
	elif keys[pygame.K_d] and player.x < screen_width - player.width - player.velocity:
		player.x += player.velocity
		player.right = True
		player.left = False
	else:
		player.right = False
		player.left = False
		player.walk_count = 0

	# JUMPING
	# no jumping in mid air or changing your trajectory during the jump
	if not(player.is_jump):
		if keys[pygame.K_SPACE]:
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

# a pygame always ends with pygame.quit()
pygame.quit()
