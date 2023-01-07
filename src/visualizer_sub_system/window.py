from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def showWindowFunc():
    global __window_global__
    __window_global__.render()

def getWindow(label: str):
    global __window_global__
    __window_global__ = Window(label)
    return __window_global__

class Window:
    shader_program = None
    vao = None

    def __init__(self, label: str):
        self.shader_program = None
        self.vao = None
        self.initWindow(label)

    def initialize(self, shader_program, vao):
        self.shader_program = shader_program
        self.vao = vao

    def startMainLoop(self):
        if self.shader_program == None or self.vao == None:
            raise ArgumentError("Shader and VAO need to be set before starting the main loop.")

        glutMainLoop()  # Keeps the window created above displaying/running in a loop
    
    def render(self):
        glUseProgram(self.shader_program)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glBindVertexArray(0)

        glutSwapBuffers()

    def initWindow(self, label: str):
        glutInit() # Initialize a glut instance which will allow us to customize our window
        glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
        glutInitWindowSize(500, 500)   # Set the width and height of your window
        glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
        self.window_handle = glutCreateWindow(label) # Give your window a title
        glutDisplayFunc(showWindowFunc)  # Tell OpenGL to call the showScreen method continuously