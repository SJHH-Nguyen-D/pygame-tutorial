import pygame
import os

sprite_dir = "/home/dennis/Desktop/Link to datascience_job_portfolio/pygame-tutorial/sprites"
pygame.init()

# create a window with which the game will happen in with width and height of window
screen_width = 500
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First Game")

# Load Sprites
walk_right = [
	pygame.image.load(os.path.join(sprite_dir, "R1.png")), 
	pygame.image.load(os.path.join(sprite_dir, "R2.png")),
	pygame.image.load(os.path.join(sprite_dir, "R3.png")),
	pygame.image.load(os.path.join(sprite_dir, "R4.png")), 
	pygame.image.load(os.path.join(sprite_dir, "R5.png")), 
	pygame.image.load(os.path.join(sprite_dir, "R6.png")), 
	pygame.image.load(os.path.join(sprite_dir, "R7.png")), 
	pygame.image.load(os.path.join(sprite_dir, "R8.png")), 
	pygame.image.load(os.path.join(sprite_dir, "R9.png"))
	]
walk_left = [
	pygame.image.load(os.path.join(sprite_dir, "L1.png")), 
	pygame.image.load(os.path.join(sprite_dir, "L2.png")),
	pygame.image.load(os.path.join(sprite_dir, "L3.png")),
	pygame.image.load(os.path.join(sprite_dir, "L4.png")), 
	pygame.image.load(os.path.join(sprite_dir, "L5.png")), 
	pygame.image.load(os.path.join(sprite_dir, "L6.png")), 
	pygame.image.load(os.path.join(sprite_dir, "L7.png")), 
	pygame.image.load(os.path.join(sprite_dir, "L8.png")), 
	pygame.image.load(os.path.join(sprite_dir, "L9.png"))
	]
bg = pygame.image.load(os.path.join(sprite_dir, "bg.jpg"))
char = pygame.image.load(os.path.join(sprite_dir, "standing.png"))
clock = pygame.time.Clock()

# setting up character dimensions
x = 50
y = 425
width = 64
height = 64
velocity = 10 # how fast our character moves

# jump code
# use a quadratic function parabola to model a jump
is_jump = False
jump_count = 10
left = False
right = False
walk_count = 0


def redraw_game_window():
	""" draw window and character sprite """
	global walk_count

	# fill background with an image with 'background lit', followed by its position
	win.blit(bg, (0, 0))z

	# Draw the character
	if walk_count + 1 >=27:
		walk_count = 0

	# Drawing our character during left movement
	if left:
		win.blit(walk_left[walk_count//3], (x, y))
		walk_count += 1
	elif right:
		win.blit(walk_right[walk_count//3], (x, y))
		walk_count += 1
	else:
		win.blit(char, (x, y))
		walk_count += 1

	pygame.display.update()


# main loop for which the game will work through
# def main():
run = True
while run:
	# checks for collision in the main-loop
	# set the frame rate of the game to 27 FPS
	clock.tick(27)

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
	if keys[pygame.K_LEFT] and x > velocity:
		x -= velocity
		right = False
		left = True
	elif keys[pygame.K_RIGHT] and x < screen_width-width-velocity:
		x -= velocity
		right = True
		left = False
	else:
		right = False
		left = False
		walk_count = 0

	# JUMPING
	# no jumping in mid air or changing your trajectory during the jump
	if not(is_jump):
		if keys[pygame.K_SPACE]:
			is_jump = True
			right = False
			left = False
			walk_count = 0
	# actually jumping
	else:
		# allow left and right during jump
		# on the up stroke of our jump
		if jump_count >= -10:
			neg = 1
			# on the down stroke of our jump
			if jump_count < 0:
				neg = -1
			# move the character up by a certain number of pixels
			y -= (jump_count **3) * 0.5 * neg
			jump_count -= 1
		else:
			is_jump = False
			jump_count = 10

	redraw_game_window()

pygame.quit()

# if __name__ == "__main__":
# 	main()