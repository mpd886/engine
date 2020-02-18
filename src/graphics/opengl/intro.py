from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


WIDTH = 500
HEIGHT = 500


def square():
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # remove everything from screen
    glLoadIdentity() # reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    square()
    glutSwapBuffers()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Intro")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
