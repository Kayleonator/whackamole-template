import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        init_mole_pos = (0, 0)
        first_run = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // 32
                    col = x // 32
                    mouse_pos = (col, row)
                    if mouse_pos == init_mole_pos and first_run:
                        first_run = False
                        mole_x = (random.randrange(0, 21))
                        mole_y = (random.randrange(0, 17))
                        mole_pos = (mole_x, mole_y)
                    elif mouse_pos == mole_pos:
                        mole_x = (random.randrange(0, 20))
                        mole_y = (random.randrange(0, 16))
                        mole_pos = (mole_x, mole_y)
                    else:
                        continue
                screen.fill((232, 226, 176))
                if first_run:
                    screen.blit(mole_image, mole_image.get_rect(topleft=init_mole_pos))
                else:
                    screen.blit(mole_image, mole_image.get_rect(topleft= (mole_x * 32 + 3, mole_y * 32 + 2)))
                for i in range(1, 20):
                    pygame.draw.line(screen, (161, 147, 84), (i * 32, 0), (i * 32, 512))
                for i in range(1, 16):
                    pygame.draw.line(screen, (161, 147, 84), (0, i * 32), (640, i * 32))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()