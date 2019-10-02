
import pygame

pygame.init()

WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
PINK = (230, 50, 230)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PI = 3.14


DISPLAY_WIDTH = 600
DISPLAY_HEIGH = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

pygame.display.set_caption("IRAS FIRST GAME")

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other
    # drawing commands above this,
    # or they will be erased with this command.

    gameDisplay.fill(ORANGE)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()

    # --- Limit to 60 frames per second
    clock.tick(60)

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # малюємо дуги
        pygame.draw.arc(gameDisplay, WHITE, (10, 50, 280, 100), 0, PI)
        pygame.draw.arc(gameDisplay, PINK, (50, 30, 200, 150), PI, 2 * PI, 3)

        # малюємо коли
        pygame.draw.circle(gameDisplay, YELLOW, (200, 300), 150,5)
        pygame.draw.circle(gameDisplay, PINK, (300, 300), 150)

        # малюємо еліпс
        pygame.draw.ellipse(gameDisplay, GREEN, (100, 300, 280, 100))

        # малюємо ламану
        pygame.draw.lines(gameDisplay, WHITE, True,
                          [[10, 10], [140, 70], [280, 20]], 2)
        pygame.draw.aalines(gameDisplay, WHITE, False,
                            [[10, 100], [140, 170], [280, 110]])
        # малюємо лінію
        pygame.draw.line(gameDisplay, WHITE, [10, 30], [290, 15], 3)
        pygame.draw.line(gameDisplay, WHITE, [10, 50], [290, 35])
        pygame.draw.aaline(gameDisplay, WHITE, [10, 70], [290, 55])

        pygame.display.update()
        clock.tick(60)