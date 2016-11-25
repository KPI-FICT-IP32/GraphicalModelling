from math import sqrt

import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Figure:
    def draw(self):
        glBegin(GL_QUADS)

        # Pyramid base
        glColor3f(1, 1, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(2, 0, 0)
        glVertex3f(2, 2, 0)
        glVertex3f(0, 2, 0)

        # Prism sides
        glColor3f(1, 0, 0)
        glVertex3f(2, 0, 0)
        glVertex3f(5, 0, 2)
        glVertex3f(5, 2, 2)
        glVertex3f(2, 2, 0)

        glColor3f(0, 1, 0)
        glVertex3f(2, 0, 0)
        glVertex3f(5, 0, 2)
        glVertex3f(4, 1, 4)
        glVertex3f(1, 1, 2)

        glColor3f(0, 0, 1)
        glVertex3f(2, 2, 0)
        glVertex3f(5, 2, 2)
        glVertex3f(4, 1, 4)
        glVertex3f(1, 1, 2)
        glEnd()

        glBegin(GL_TRIANGLES)
        # Pyramid sides
        glColor3f(1, 1, 0)
        glVertex3f(2, 2, 0)
        glVertex3f(1, 1, 2)
        glVertex3f(0, 2, 0)

        glColor3f(1, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(1, 1, 2)
        glVertex3f(0, 2, 0)

        glColor3f(0, 1, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(1, 1, 2)
        glVertex3f(2, 0, 0)

        # Prism base
        glColor3f(1, 0, 1)
        glVertex3f(5, 0, 2)
        glVertex3f(5, 2, 2)
        glVertex3f(4, 1, 4)
        glEnd()


def main():
    fig = Figure()
    pygame.init()
    display = (display_x, display_y) = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)   
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, display_x/display_y, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -12)
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.5, 0, 0, 1)
        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        fig.draw()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
