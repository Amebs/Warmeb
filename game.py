import pygame
from pygame import *

width = 800
height = 640
display = (width, height)
bag_color = "#004400"
black = [0, 0, 0]
x = 100
y = 100


def test(xy):
    pygame.draw.line(xy, black, [x - 30, y - 50], [x + 30, y - 50], 5)
    pygame.draw.line(xy, black, [x + 30, y - 50], [x + 60, y], 5)
    pygame.draw.line(xy, black, [x + 60, y], [x + 30, y + 50], 5)
    pygame.draw.line(xy, black, [x + 30, y + 50], [x - 30, y + 50], 5)
    pygame.draw.line(xy, black, [x - 30, y + 50], [x - 60, y], 5)
    pygame.draw.line(xy, black, [x - 60, y], [x - 30, y - 50], 5)


def main():
    pygame.init()
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption("Warmeb")
    bg = Surface((width, height))

    bg.fill(Color(bag_color))

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit, "QUIT"
        screen.blit(bg, (0, 0))

        test(screen)
	x=x+60

        pygame.display.update()

if __name__ == "__main__":
    main()
