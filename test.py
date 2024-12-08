from lumikki import codes, to_symbols, to_numbers
import pygame, random


pygame.init()


SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
PIXEL_SIZE = 4

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lumikki Tool")


pixel_x = (SCREEN_WIDTH // 2)
pixel_y = (SCREEN_HEIGHT // 2)
pixel_color = (255, 0, 0)

speed = PIXEL_SIZE


clock = pygame.time.Clock()


pixel_positions = []

order: str = "1234"

running = True

# accidental infinite loop oops
while running:
    for c in range(len(codes)):
        for i in range(len(codes[c])):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # keys = pygame.key.get_pressed()

            if codes[c][i] == "←":
                pixel_x -= speed

            elif codes[c][i] == "→":
                pixel_x += speed

            elif codes[c][i] == "↑":
                pixel_y -= speed

            elif codes[c][i] == "↓":
                pixel_y += speed

            if codes[c][i] == "•":
                pixel_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # Rotate clockwise the whole pattern
                """
                order: str = order[1:] + order[0]
                d = to_numbers(codes[c], "0"+order)
                codes[c] = to_symbols(d)
                """

            pixel_positions.append((pixel_x, pixel_y, pixel_color))

            for pos in pixel_positions:
                pygame.draw.rect(screen, pos[2], (pos[0], pos[1], PIXEL_SIZE, PIXEL_SIZE))

            pygame.display.update()
            clock.tick(144)

pygame.quit()
