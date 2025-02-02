import pygame
import os
import math
from tezzeract import tezzeract_multiplication

os.environ["SDL_VIDEO_CENTERED"]='1'
black, white, blue  = (5, 6, 6), (230, 230, 230), (0, 154, 255)
width, height = 1920, 1080

pygame.init()
pygame.display.set_caption("4D cube Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60

angle = 0
cube_position = [width//2, height//2]
scale = 4000
speed = 0.01
points = [n for n in range(16)]

points[0] = [[-1], [-1], [1], [1]]
points[1] = [[1], [-1], [1], [1]]
points[2] = [[1], [1], [1], [1]]
points[3] = [[-1], [1], [1], [1]]
points[4] = [[-1], [-1], [-1], [1]]
points[5] = [[1], [-1], [-1], [1]]
points[6] = [[1], [1], [-1], [1]]
points[7] = [[-1], [1], [-1], [1]]
points[8] = [[-1], [-1], [1], [-1]]
points[9] = [[1], [-1], [1], [-1]]
points[10] = [[1], [1], [1], [-1]]
points[11] = [[-1], [1], [1], [-1]]
points[12] = [[-1], [-1], [-1], [-1]]
points[13] = [[1], [-1], [-1], [-1]]
points[14] = [[1], [1], [-1], [-1]]
points[15] = [[-1], [1], [-1], [-1]]


def connect_point(i, j, k, offset):
    a = k[i + offset]
    b = k[j + offset]
    pygame.draw.line(screen, white, (a[0], a[1]), (b[0], b[1]), 3)


run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False

    index = 0
    projected_points = [j for j in range(len(points))]

    #3d tezzeract rotations
    rotation_x = [[1, 0, 0],
                  [0, math.cos(angle), -math.sin(angle)],
                  [0, math.sin(angle), math.cos(angle)]]

    rotation_y = [[math.cos(angle), 0, -math.sin(angle)],
                  [0, 1, 0],
                  [math.sin(angle), 0, math.cos(angle)]]

    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                  [math.sin(angle), math.cos(angle), 0],
                  [0, 0 ,1]]
    tesseract_rotation = [[1, 0, 0],
                          [0, math.cos(-math.pi/2), -math.sin(-math.pi/2)],
                          [0, math.sin(-math.pi/2), math.cos(-math.pi/2)]]
    #4d tezzeract rotations

    rotation4d_xy= [[math.cos(angle), -math.sin(angle), 0, 0],
                  [math.sin(angle), math.cos(angle), 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]]
    rotation4d_xz = [[math.cos(angle), 0, -math.sin(angle), 0],
                     [0, 1, 0, 0],
                     [math.sin(angle), 0, math.cos(angle), 0],
                     [0, 0, 0, 1]]
    rotation4d_xw = [[math.cos(angle), 0, 0, -math.sin(angle)],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [math.sin(angle), 0, 0, math.cos(angle)]]
    rotation4d_yz = [[1, 0, 0, 0],
                     [0, math.cos(angle), -math.sin(angle), 0],
                     [0, math.sin(angle), math.cos(angle), 0],
                     [0, 0, 0, 1]]
    rotation4d_yw = [[1, 0, 0, 0],
                     [0, math.cos(angle), 0, -math.sin(angle)],
                     [0, 0, 1, 0],
                     [0, math.sin(angle), 0, math.cos(angle)]]
    rotation4d_zw = [[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, math.cos(angle), -math.sin(angle)],
                     [0, 0, math.sin(angle), math.cos(angle)]]

    for point in points:

        rotated_3d = tezzeract_multiplication(rotation4d_xy, point)
        rotated_3d = tezzeract_multiplication(rotation4d_zw, rotated_3d)

        distance = 5
        w = 1/(distance - rotated_3d[3][0])
        projection_tezzeract4 = [
                            [w, 0, 0, 0],
                            [0, w, 0, 0],
                            [0, 0, w, 0],]

        projected_3d = tezzeract_multiplication(projection_tezzeract4, rotated_3d)
        rotated_2d = tezzeract_multiplication(tesseract_rotation, projected_3d)
        z = 1/(distance - (rotated_2d[2][0] + rotated_3d[3][0]))
        projection_tezzeract = [[z, 0, 0],
                            [0, z, 0 ]
                            ]

        rotated_2d = tezzeract_multiplication(rotation_x, projected_3d)
        projected_2d = tezzeract_multiplication(projection_tezzeract, rotated_2d)
        x = int(projected_2d[0][0] * scale) + cube_position[0]
        y = int(projected_2d[1][0] * scale) + cube_position[1]

        projected_points[index] = [x, y]
        pygame.draw.circle(screen, blue, (x, y), 10)
        index += 1
    #draw edges
    for m in range(4):
        connect_point(m, (m+1)%4, projected_points, 8)
        connect_point(m+4, (m+1)%4 + 4, projected_points, 8)
        connect_point(m, m+4, projected_points, 8)

    for m in range(4):
        connect_point(m, (m+1)%4, projected_points, 0)
        connect_point(m+4, (m+1)%4 + 4, projected_points, 0)
        connect_point(m, m+4, projected_points, 0)

    for m in range(8):
        connect_point(m,  m+8, projected_points, 0)

    angle += speed
    pygame.display.update()

pygame.quit()
