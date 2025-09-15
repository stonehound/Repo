import pygame

# 1. Initialize Pygame and set up the display
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Translate Shape")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 2. Define the shape's position and speed
# Use a Rect object for easy positioning and movement
shape_rect = pygame.Rect(50, 50, 50, 50) # (x, y, width, height)
speed_x = 30
speed_y = 30

# Game loop variables
running = True
clock = pygame.time.Clock()

# 3. Main game loop
while running:
    # 4. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 5. Update the shape's position
    # The .move_ip() method moves the rectangle in-place by the given offset
    shape_rect.move_ip(speed_x, speed_y)

    #  Handle collision with screen edges to "bounce" the shape
    if shape_rect.left < 0 or shape_rect.right > screen_width:
        speed_x = -speed_x # Reverse x-direction
    if shape_rect.top < 0 or shape_rect.bottom > screen_height:
        speed_y = -speed_y # Reverse y-direction

    # 6. Clear the screen (erase the previous frame)
    screen.fill(WHITE)

    # 7. Draw the shape at its new position
    pygame.draw.rect(screen, BLUE, shape_rect)

    # 8. Update the display to show the changes
    pygame.display.flip()

    # 9. Control the frame rate
    clock.tick(120) # Limits the game to 60 frames per second

# 10. Quit Pygame
pygame.quit()

