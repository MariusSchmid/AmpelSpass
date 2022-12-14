#version 400
layout (location = 0) in vec2 aPos;

out vec2 aCol;

void main()
{
    aCol = aPos;
    gl_Position = vec4(aPos.x, aPos.y, 0.0, 1.0);
}