import pygame
pygame.init()

# create a window with which the game will happen in with width and height of window
screen_width = 500
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First Game")

# setting up character dimensions
x = 50
y = 450
width = 40
height = 60
velocity = 10 # how fast our character moves

# jump code
# use a quadratic function parabola to model a jump
is_jump = False
jump_count = 10


# main loop for which the game will work through
# usually all loops start with while
# def main():
run = True
while run:
	# checks for collision in the main-loop
	pygame.time.delay(100) # time delay clock in milliseconds

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
	
	# and if our character is moving left, we have to make sure that our character's position is 
	# greater than 0, otherwise we would be moving off the screen
	if keys[pygame.K_LEFT] and x > velocity:
		x -= velocity

	if keys[pygame.K_RIGHT] and x < screen_width-width-velocity:
		x -= velocity

	# no jumping in mid air or changing your trajectory during the jump
	if not(is_jump):
		if keys[pygame.K_UP] and y > velocity:
			y -= velocity

		if keys[pygame.K_DOWN] and y < height-height-velocity:
			y += velocity

		if keys[pygame.K_SPACE]:
			is_jump = True
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

	win.fill((0, 0, 0))

	# create a rectangle that is going to represent our character
	# all objects in the game require the first argument to happen in the window
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.update()

pygame.quit()

# if __name__ == "__main__":
# 	main()