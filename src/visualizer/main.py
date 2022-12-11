import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
print("Imports successful!") # If you see this printed to the console then installation was successful

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)


glutInit() # Initialize a glut instance which will allow us to customize our window
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the width and height of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Coding Practice") # Give your window a title
glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times

def compileShader(shader_type, source):

    import ipdb; ipdb.set_trace();
    shader = glCreateShader(shader_type) # e.g GL_VERTEX_SHADER
    glShaderSource(shader, 1, source, len(source))
    glCompileShader(shader)
    isCompiled = 0
    glGetShaderiv(shader, GL_COMPILE_STATUS, isCompiled)

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

    isLinked = 0
    glGetProgramiv(program, GL_LINK_STATUS, isLinked)
    if isLinked == GL_FALSE:
        print("Failed to link shader")
        exit(1)

    glDetachShader(program, vertex_shader)
    glDetachShader(program, fragment_shader)

    return program

program = compileProgram("src/visualizer/shaders/default.frag", "src/visualizer/shaders/default.vert")

glutMainLoop()  # Keeps the window created above displaying/running in a loop