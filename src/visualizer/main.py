import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import numpy
import utils


glutInit() # Initialize a glut instance which will allow us to customize our window
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the width and height of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Coding Practice") # Give your window a title

def compileShader(shader_type, source):
    shader = glCreateShader(shader_type) # e.g GL_VERTEX_SHADER
    glShaderSource(shader, source)
    glCompileShader(shader)
    isCompiled = glGetShaderiv(shader, GL_COMPILE_STATUS)

    if isCompiled == GL_FALSE:
        print("Failed to compile shader")
        exit(1)

    return shader

def compileProgram(vertex_path, fragment_path):
    vertex_file = open(vertex_path, "r")
    vertex_source = vertex_file.read()

    fragment_file = open(fragment_path, "r")
    fragment_source = fragment_file.read()

    vertex_shader = compileShader(GL_VERTEX_SHADER, vertex_source)
    fragment_shader = compileShader(GL_FRAGMENT_SHADER, fragment_source)

    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    isLinked = glGetProgramiv(program, GL_LINK_STATUS)
    if isLinked == GL_FALSE:
        print("Failed to link shader")
        exit(1)

    glDetachShader(program, vertex_shader)
    glDetachShader(program, fragment_shader)

    return program

global program
root_dir = utils.getRootDir()
program = compileProgram(root_dir + "/src/visualizer/shaders/default.vert", root_dir + "/src/visualizer/shaders/default.frag")
glUseProgram(program)

global vao
vao = glGenVertexArrays(1)
glBindVertexArray(vao)

verts = [-1, -1, 1, -1, 0, 1]
vbuf = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbuf)
glBufferData(GL_ARRAY_BUFFER, (ctypes.c_float * len(verts))(*verts), GL_STATIC_DRAW)
glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
glEnableVertexAttribArray(0)

glBindBuffer(GL_ARRAY_BUFFER, 0)
glBindVertexArray(0)

def showScreen():
    glUseProgram(program)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(0)

    glutSwapBuffers()

glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously

glutMainLoop()  # Keeps the window created above displaying/running in a loop