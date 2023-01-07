from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

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