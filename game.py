import pygame
from pygame import *
import math

width = 800
height = 640
display = (width, height)
bag_color = "#004400"
black = [0, 0, 0]
x = 100
y = 100
point = [100, 100]


def draw_hexapod(screen, point):
    hexagon = []
    for i in range(0, 6):
        hexagon.append(hex_corner(point[0], point[1], 50, i))
    for i in range(0, 5):
            pygame.draw.line(screen, black, hexagon[i], hexagon[i+1], 5)
    pygame.draw.line(screen, black, hexagon[5], hexagon[0], 5)


def hex_corner(center_x, center_y, size, i):
    point_xy = [0, 0]
    angle_deg = 60 * i + 30
    angle_rad = math.pi / 180 * angle_deg
    point_xy[0] = center_x + size * math.cos(angle_rad)
    point_xy[1] = center_y + size * math.sin(angle_rad)
    return point_xy


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
        for i in range(0,10):
            draw_hexapod(screen, point)
            point[0] += 90
        point[0] = 100
        point[1] = 100
        test(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
