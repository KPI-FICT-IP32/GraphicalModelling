from math import sqrt

import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class CutPyramid:
    vertices = (
        # Bottom triangle
        (0.0, 0.0, 0.0),
        (sqrt(3)/2, 0.0, 0.5),
        (0.0, 0.0, 1.0),

        # Top triangle
        (0.2, 0.5, 0.2),
        (sqrt(3)/2 - 0.2, 0.5, 0.5),
        (0.2, 0.5, 0.8),
    )

    edges = (
        # Bottom base
        (0, 1), (0, 2), (1, 2),
        # Top base
        (3, 4), (3, 5), (4, 5),

        # Connections between bases
        (0, 3), (1, 4), (2, 5),
    )

    def draw(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()


def main():
    fig = CutPyramid()
    pygame.init()
    display = (display_x, display_y) = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display_x / display_y), 1.0, 50.0)
    glTranslatef(0.0,0.0, -3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.5, 1, 0, 0)
        glRotatef(1, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        fig.draw()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
