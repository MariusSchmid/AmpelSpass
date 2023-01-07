from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from .utils import getRootDir
from .window import getWindow
from .shaderUtils import compileProgram

def start_visualizer_subsystem():
    main_window = getWindow("AmpelSpass")

    root_dir = getRootDir()
    shaders_dir = root_dir + "/src/visualizer_sub_system/shaders/"
    program = compileProgram(shaders_dir + "/default.vert", shaders_dir + "/default.frag")
    glUseProgram(program)

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

    main_window.initialize(program, vao)
    main_window.startMainLoop()