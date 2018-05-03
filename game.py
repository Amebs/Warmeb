import pygame
from pygame import *
import math

width = 800
height = 640
display = (width, height)
bag_color = "#004400"
hex_color_1 = [200, 200, 200, 200]
hex_color_2 = [10, 30, 70, 100]
black = [200, 200, 200]
global radius
radius = 10
fat = 1
point = [0, 0]
point_new = [0, 0]
global kx
global ky
kx = 4
ky = 4
point_new[0] = kx*radius * 3 / 2
point_new[1] = ky*2 * (math.sqrt(3) / 2 * radius)
startxy = [0, 0]
global zaliv
zaliv = int((math.sqrt(3) * radius / 2)+1)


####123
def draw_hexapod(screen, point, radius):
    hexagon = []
    for i in range(0, 6):
        hexagon.append(hex_corner(point[0], point[1], radius, i))
    for i in range(0, 5):
        pygame.draw.line(screen, black, hexagon[i], hexagon[i+1], fat)
    pygame.draw.line(screen, black, hexagon[5], hexagon[0], fat)


def draw_hexagon(screen, point, radius, hex_color):
   hexagon = []
   for i in range(0, 6):
       hexagon.append(hex_corner(point[0], point[1], radius, i))
   for i in range(0, 5):
       pygame.draw.polygon(screen, hex_color, hexagon, 1)


def hex_corner(center_x, center_y, size, i):
   point_xy = [0, 0]
   angle_deg = 60 * i
   angle_rad = math.pi / 180 * angle_deg
   point_xy[0] = center_x + size * math.cos(angle_rad)
   point_xy[1] = center_y + size * math.sin(angle_rad)
   return point_xy

def field(screen, point, radius, hex_color):
   for n in range(0, 50):
       for i in range(0, 50):
           if (i % 2):
               draw_hexagon(screen, point, radius, hex_color)
               point[0] = i * radius * 3 / 2
               point[1] = math.sqrt(3) / 2 * radius + n * 2 * (math.sqrt(3) / 2 * radius)
           else:
               draw_hexagon(screen, point, radius, hex_color)
               point[0] = i * radius * 3 / 2
               point[1] = n * 2 * (math.sqrt(3) / 2 * radius)


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

           if e.type == pygame.KEYDOWN:

               global point_new
               global radius
               global fat
               global kx
               global ky

               if e.key == pygame.K_END:
                   bg.fill(Color("#55ffff"))

               if e.key == pygame.K_PAGEDOWN:
                   point_new[0] += 3*radius/2
                   point_new[1] += (math.sqrt(3) / 2 * radius)

               if e.key == pygame.K_DELETE:
                   point_new[0] -= 3*radius/2
                   point_new[1] += (math.sqrt(3) / 2 * radius)

               if e.key == pygame.K_DOWN:
                   ky = ky + 1
                   #point_new[1] += 2 * (math.sqrt(3) / 2 * radius)

               if e.key == pygame.K_UP:
                   ky = ky - 1
                   #point_new[1] -= 2 * (math.sqrt(3) / 2 * radius)


               if e.key == pygame.K_RIGHT:
                   kx = kx + 2
                   #point_new[0] += 3*radius

               if e.key == pygame.K_LEFT:
                   kx = kx - 2
                   #point_new[0] -= 3*radius

           if e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
               #left mouse button
               radius
               radius=radius+10

               break
           if e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
               #right mouse button
               radius
               if radius>10:
                   radius = radius-10

               #field(screen, point, radius)
               #startxy[0] += 50
               #startxy[1] += 50
               break
       screen.blit(bg, startxy)
       field(screen, point, radius, hex_color_2)
       fat = 3
       point_new[0] = kx * radius * 3 / 2
       point_new[1] = ky * 2 * (math.sqrt(3) / 2 * radius)
       draw_hexapod(screen, point_new, radius)
       pygame.draw.circle(screen, hex_color_1, [int(point_new[0]), int(point_new[1])], zaliv)
       point[0] = 0 # x
       point[1] = 0 # y
       pygame.display.update()


if __name__ == "__main__":
   main()
