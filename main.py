import pygame
pygame.init()

# create a window with which the game will happen in with width and height of window
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

# setting up character dimensions
x = 50
y = 50
width = 40
height = 60
velocity = 5 # how fast our character moves

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
	
	if keys[pygame.K_LEFT]:
		x -= velocity

	if keys[pygame.K_RIGHT]:
		x -= velocity

	if keys[pygame.K_UP]:
		y -= velocity

	if keys[pygame.K_DOWN]:
		y += velocity

	win.fill((0, 0, 0))

	# create a rectangle that is going to represent our character
	# all objects in the game require the first argument to happen in the window
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.update()


pygame.quit()

# if __name__ == "__main__":
# 	main()