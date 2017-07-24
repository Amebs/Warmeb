import pygame
from pygame import *
import math

width = 800
height = 640
display = (width, height)
bag_color = "#004400"
black = [0, 0, 0]
x = 0
y = 0
point = [0, 0]


def draw_hexapod(screen, point):
    hexagon = []
    for i in range(0, 6):
        hexagon.append(hex_corner(point[0], point[1], 50, i))
    for i in range(0, 5):
            pygame.draw.line(screen, black, hexagon[i], hexagon[i+1], 2)
    pygame.draw.line(screen, black, hexagon[5], hexagon[0], 2)


def hex_corner(center_x, center_y, size, i):
    point_xy = [0, 0]
    angle_deg = 60 * i + 30
    angle_rad = math.pi / 180 * angle_deg
    point_xy[1] = center_x + size * math.cos(angle_rad)
    point_xy[0] = center_y + size * math.sin(angle_rad)
    return point_xy


def test(xy):
    pygame.draw.line(xy, black, [x - 30, y - 50], [x + 30, y - 50], 5)
    pygame.draw.line(xy, black, [x + 30, y - 50], [x + 60, y], 5)
    pygame.draw.line(xy, black, [x + 60, y], [x + 30, y + 50], 5)
    pygame.draw.line(xy, black, [x + 30, y + 50], [x - 30, y + 50], 5)
    pygame.draw.line(xy, black, [x - 30, y + 50], [x - 60, y], 5)
    pygame.draw.line(xy, black, [x - 60, y], [x - 30, y - 50], 5)

def range_point_chet(point):
    point[0] += math.sqrt(3) * 50
    return point[0]

def stroka(screen, point):
    for i in range(0, 3):
        draw_hexapod(screen, point)
        point[1] += 150
    point[1] = 100  # x

def range_point_netchet(point):
    point[0] += math.sqrt(3)/2 * 50
    return point[0]

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


        '''for i in range(0, 3):
            stroka(screen, point)
            point[0] = range_point_chet(point)
        point[1] += 75
        for i in range(0, 3):
            stroka(screen, point)
            point[0] = range_point_netchet(point)'''
        for n in range(0, 50):
            for i in range(0,50):
                if (i%2):
                    draw_hexapod(screen, point)
                    point[1] = i * 50 * 3 / 2
                    point[0] = math.sqrt(3) / 2 * 50+n*2*(math.sqrt(3) / 2 * 50)
                else:
                    draw_hexapod(screen, point)
                    point[1] = i * 50 * 3 / 2
                    point[0] = n*2*(math.sqrt(3) / 2 * 50)




        '''for i in range(0,8):
            draw_hexapod(screen, point)
            point[1] += 100*3/2

        point[0] = 100  # y
        point[1] = 100  # x
        point[0] += math.sqrt(3) / 2 * 50
        point[1] += 50 * 3 / 2'''



        '''for i1 in range(0, 8):
            draw_hexapod(screen, point)
            point[1] += 100 * 3 / 2'''

        '''#point[0] = 100  # y
        point[1] = 100  # x
        point[0] += math.sqrt(3) / 2 * 50
        for i1 in range(0, 8):
            draw_hexapod(screen, point)
            point[1] += 100 * 3 / 2'''

        point[0] = 0 #  y
        point[1] = 0 #  x
        #test(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
