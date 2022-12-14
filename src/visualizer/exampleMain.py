from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import ctypes
import sys

name = 'PyOpenGL Example'
vao = None
program = None

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitContextVersion(4,0)
    glutInitWindowSize(600,400)
    glutCreateWindow(name)

    print(glGetString(GL_VERSION))

    glClearColor(0,0,0,1)

    glutDisplayFunc(display)
    # glutMouseFunc(callback)
    # glutMotionFunc(callback)
    # glutPassiveMotionFunc(callback)
    # glutKeyboardFunc(callback)
    # glutSpecialFunc(callback)

    vshader = glCreateShader(GL_VERTEX_SHADER)
    fshader = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vshader,["""
        #version 400

        uniform mat4 u_model;
        uniform mat4 u_view;

        in vec4 a_pos;
        in vec4 a_color;
        in vec4 a_normal;

        out vec4 v_color;
        out vec4 v_normal;

        void main() {
            gl_Position = a_pos; // * u_model * u_view;
            v_color = a_color;
            v_normal = normalize(a_normal);
        }
    """])
    glCompileShader(vshader)
    msg = glGetShaderInfoLog(vshader)
    if msg:
        print(f"Failed to compile Vertex Shader: {msg}")
        exit(0)

    glShaderSource(fshader,["""
        #version 400

        uniform mat4 u_model;
        uniform mat4 u_view;

        in vec4 v_color;
        in vec4 v_normal;

        layout(location=0) out vec4 f_color;

        void main() {
            f_color = v_color;
        }
    """])
    glCompileShader(fshader)
    msg = glGetShaderInfoLog(fshader)
    if msg:
        print(f"Failed to compile Fragment Shader: {msg}")
        exit(0)

    global program
    program = glCreateProgram()

    glAttachShader(program,vshader)
    glAttachShader(program,fshader)

    glLinkProgram(program)
    msg = glGetProgramInfoLog(program)
    if msg:
        print(f"Failed to link Program: {msg}")
        exit(0)

    glUseProgram(program)

    uniforms = {
        'model': glGetUniformLocation(program,'u_model'),
        'view': glGetUniformLocation(program,'u_view'),
    }
    print(uniforms)

    attrs = {
        'pos': glGetAttribLocation(program,'a_pos'),
        'color': glGetAttribLocation(program,'a_color'),
        'normal': glGetAttribLocation(program,'a_normal'),
    }
    print(attrs)

    global vao
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    verts = [
        -1, -1, 0, 1,
        1, -1, 0, 1,
        0, 1, 0, 1,
    ]
    colors = [
        1, 1, 1, 1,
        1, 1, 1, 1,
        1, 1, 1, 1,
    ]
    normals = [
        0, 0, 1, 0,
        0, 0, 1, 0,
        0, 0, 1, 0,
    ]

    vbuf,cbuf,nbuf = glGenBuffers(3)
    glBindBuffer(GL_ARRAY_BUFFER,vbuf)
    glBufferData(GL_ARRAY_BUFFER,(ctypes.c_float*len(verts))(*verts),GL_STATIC_DRAW)
    glVertexAttribPointer(attrs['pos'],4,GL_FLOAT,GL_FALSE,0,None)
    glEnableVertexAttribArray(attrs['pos'])

    glBindBuffer(GL_ARRAY_BUFFER,cbuf)
    glBufferData(GL_ARRAY_BUFFER,(ctypes.c_float*len(colors))(*colors),GL_STATIC_DRAW)
    glVertexAttribPointer(attrs['color'],4,GL_FLOAT,GL_FALSE,0,None)
    glEnableVertexAttribArray(attrs['color'])

    glBindBuffer(GL_ARRAY_BUFFER,nbuf)
    glBufferData(GL_ARRAY_BUFFER,(ctypes.c_float*len(normals))(*normals),GL_STATIC_DRAW)
    # glVertexAttribPointer(attrs['normal'],4,GL_FLOAT,GL_FALSE,0,0)
    # glEnableVertexAttribArray(attrs['normal'])

    glBindBuffer(GL_ARRAY_BUFFER,0)
    glBindVertexArray(0)

    identity = [
        1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1,
    ]
    # glUniformMatrix4fv(uniforms['model'],1,GL_FALSE,(ctypes.c_float*16)(*identity))
    # glUniformMatrix4fv(uniforms['view'],1,GL_FALSE,(ctypes.c_float*16)(*identity))

    glutMainLoop()
    return

def display():
    glUseProgram(program)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glViewport(0,0,600,400)

    print(vao)
    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES,0,3)
    glBindVertexArray(0)

    glutSwapBuffers()
    return

def callback(*args):
    print(*args)

if __name__ == '__main__': main()