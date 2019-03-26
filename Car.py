from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np
from math import *

Angle = 0
forward = True
x = 0
car_z=0
def keyBoardArrows(key, x, y):
    global car_z
    if key == GLUT_KEY_LEFT:
        car_z -= 0.5
    elif key == GLUT_KEY_RIGHT:
        car_z += 0.5
def init():
     glClearColor(1, 1, 1, 1)
     glMatrixMode(GL_PROJECTION)
     gluPerspective(60 ,1 ,0.1 ,30)
     # glMatrixMode(GL_MODELVIEW) that's the cause of the problem
     gluLookAt(6, 9, 10,  #eye:the place of the camera
               0, 0, 0,   #center:the place of the model which the camera look at
               0, 1, 0)   #up:the camera direction of viewing
     glClear(GL_COLOR_BUFFER_BIT)
def draw():
    global car_z
    global Angle
    global x
    global forward
    glLineWidth(10)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    def draw_cirle(r=0.5, x1=0.2, x2=0.02, x3=0, color=(0,0,0)):
        glColor3f(color[0],color[1],color[2])
        glBegin(GL_POLYGON)
        for theta in np.arange(0, 2 * pi, 0.01):
            # glColor3f(1-theta/(2*pi) ,theta/2*pi ,1)
            x = r * cos(theta)
            y = r * sin(theta)
            glVertex(x + x1, y + x2, x3)
        glEnd()

    #the ground
    glColor(119 / 255, 136 / 255, 153 / 255)
    glBegin(GL_QUADS)
    glVertex(-30, 0, 50)
    glVertex(-30, 0, -50)
    glVertex(30, 0, -50)
    glVertex(30, 0, 50)
    glEnd()

    # lines besides the car
    for color_z in range(-20, 20, 3):
       if color_z & 1 == 1:
           glColor(0, 0, 0)
           glBegin(GL_QUADS)
           glVertex(5, 0, color_z+3)
           glVertex(6, 0, color_z+3)
           glVertex(6, 0, color_z-4)
           glVertex(5, 0, color_z-4)
           glVertex(-5, 0, (color_z+3))
           glVertex(-6, 0, color_z+3)
           glVertex(-6, 0, (color_z-4))
           glVertex(-5, 0, (color_z-4))
           glEnd()
       else:
           glColor(1, 1, 1)
           glBegin(GL_QUADS)
           glVertex(5, 0, color_z+3)
           glVertex(6, 0, color_z+3)
           glVertex(6, 0, color_z-4)
           glVertex(5, 0, color_z-4)
           glVertex(-5, 0, (color_z + 3))
           glVertex(-6, 0, color_z + 3)
           glVertex(-6, 0, (color_z - 4))
           glVertex(-5, 0, (color_z - 4))
           glEnd()

    # the white lines in the middle
    for white in range(-30, 10, 5):
        if white & 1 == 0:
            glBegin(GL_QUADS)
            glColor(1, 1, 1)
            glVertex(-0.25, 0, white)
            glVertex(0.25, 0, white)
            glVertex(0.25, 0, white+7)
            glVertex(-0.25, 0, white+7)
            glEnd()
        else:
            pass

# the sun
    draw_cirle(1, -6.55, 6.5, -1, (1, 140/255, 0))

#trees
    for tree in range(-30, 20, 3):
        if tree & 1 == 0:
            glBegin(GL_QUADS)
            glColor(105/255, 105/255, 105/255)
            glVertex(-8, 4, tree)
            glVertex(-8, 0, tree)
            glVertex(-8, 0, tree+0.5)
            glVertex(-8, 4, tree+0.5)
            glEnd()
        else:
            pass

    for tree in range(-30, 20, 3):
        if tree & 1 == 0:
             glColor(0 / 255, 255 / 255, 0 / 255)
             draw_cirle(1.5,-8, 4, tree, (0 / 255, 255 / 255, 0 / 255))
        else:
            pass

    glLoadIdentity()
    glColor3f(1, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(x, 0 ,0+car_z)
    glScale(1, .25, .5)
    glutWireCube(5)

    glLoadIdentity()
    glColor3f(1, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(x, 5 * .25, 0+car_z)
    glScale(.5, .25, .5)
    glutWireCube(5)

    # right front torus
    glLoadIdentity()
    glColor(0 ,0 ,1)
    glRotate(90, 0, 1, 0)
    glTranslate(2.5+x ,0 ,-1.25+car_z)
    glRotate(Angle, 0, 0, 1)
    glutWireTorus(0.2, 0.5 ,12 ,8)

    # left front torus
    glLoadIdentity()
    glColor(0, 0, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(2.5+x, 0, 1.25+car_z)
    glRotate(Angle, 0, 0, 1)
    glutWireTorus(0.2, 0.5, 12, 8)

    # right behind torus
    glLoadIdentity()
    glColor(0, 0, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-2.5+x, 0, -1.25+car_z)
    glRotate(Angle, 0, 0, 1)
    glutWireTorus(0.2, 0.5, 12, 8)
    # left behind torus
    glLoadIdentity()
    glColor(0, 0, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-2.5+x, 0, 1.25+car_z)
    glRotate(Angle, 0, 0, 1)
    glutWireTorus(0.2, 0.5, 12, 8)

    if forward:
        Angle-=0.1
        x+=0.1
        if x>10:
            forward=False
    else:
        Angle+=0.1
        x-=0.1
        if x<-5:
            forward=True

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutInitWindowPosition(930, 50)
glutCreateWindow(b"CAR")
glutDisplayFunc(draw)
glutSpecialFunc(keyBoardArrows)

init()
glutIdleFunc(draw)
glutMainLoop()
