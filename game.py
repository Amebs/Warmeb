import pygame
from pygame import *
import math

width = 800
height = 640
display = (width, height)
bag_color = "#004400"
black = [0, 0, 0]
radius = 30
fat = 2
point = [0, 0]


def draw_hexapod(screen, point):
    hexagon = []
    for i in range(0, 6):
        hexagon.append(hex_corner(point[0], point[1], radius, i))
    for i in range(0, 5):
            pygame.draw.line(screen, black, hexagon[i], hexagon[i+1], fat)
    pygame.draw.line(screen, black, hexagon[5], hexagon[0], fat)


def hex_corner(center_x, center_y, size, i):
    point_xy = [0, 0]
    angle_deg = 60 * i
    angle_rad = math.pi / 180 * angle_deg
    point_xy[0] = center_x + size * math.cos(angle_rad)
    point_xy[1] = center_y + size * math.sin(angle_rad)
    return point_xy


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


        for n in range(0, 50):
            for i in range(0,50):
                if (i%2):
                    draw_hexapod(screen, point)
                    point[0] = i * radius * 3 / 2
                    point[1] = math.sqrt(3) / 2 * radius+n*2*(math.sqrt(3) / 2 * radius)
                else:
                    draw_hexapod(screen, point)
                    point[0] = i * radius * 3 / 2
                    point[1] = n*2*(math.sqrt(3) / 2 * radius)


        point[0] = 0 #  x
        point[1] = 0 #  y
        pygame.display.update()


if __name__ == "__main__":
    main()
