import ctypes # Lower level Python interactions
import pyglet

# It causes problems on MacOS if enabled
pyglet.options["shadow_window"] = False
# Tanks performance if enabled
pyglet.options["debug_gl"] = False

import pyglet.gl as gl


# Add data to the VBO
vertex_positions = [
    -0.5, 0.5, 1.0,
    -0.5, -0.5, 1.0,
    0.5, -0.5, 1.0,
    0.5, 0.5, 1.0,
]

# Using 2 triangles together to make a square
indices = [
    0, 1, 2, # first triangle
    0, 2, 3, # second triangle
]

class Window(pyglet.window.Window):
    def __init__(self, **args):
        super(Window, self).__init__(**args)

        # Create a vertex array object (contains multiple vertex buffer objects)
        self.vao = gl.GLuint(0)
        gl.glGenVertexArrays(1, ctypes.byref(self.vao))
        gl.glBindVertexArray(self.vao)

        # Create a vertex buffer object
        self.vbo = gl.GLuint(0)
        gl.glGenBuffers(1, ctypes.byref(self.vbo))
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        # Put the data in the VBO
        gl.glBufferData(gl.GL_ARRAY_BUFFER,
                        ctypes.sizeof(gl.GLfloat * len(vertex_positions)),
                        (gl.GLfloat * len(vertex_positions)) (*vertex_positions),
                        gl.GL_STATIC_DRAW)

        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, 0)
        gl.glEnableVertexAttribArray(0)

        # create index buffer object

        self.ibo = gl.GLuint(0)
        gl.glGenBuffers(1, self.ibo)
        gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, self.ibo)

        gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER,
                        ctypes.sizeof(gl.GLuint * len(indices)),
                        (gl.GLuint * len(indices)) (*indices),
                        gl.GL_STATIC_DRAW)

    # Called when screen is updated(?)
    def on_draw(self):
        gl.glClearColor(1.0, 0.5, 1.0, 1.0)
        self.clear()

        gl.glDrawElements(
            gl.GL_TRIANGLES,
            len(indices),
            gl.GL_UNSIGNED_INT,
            None
        )

    # Called when screen is resized
    def on_resize(self, width, height):
        print(f"Resize {width} * {height}")


class Game:
    def __init__(self):
        # Allows the use of modern OpenGL
        self.config = gl.Config(major_version=3)
        self.window = Window(config=self.config, width=800, height=600, caption="Minecraft clone",
                             resizable=True, vsync=False)  # VSync cause problems with Pyglet on some computers

    def run(self):
        pyglet.app.run()


if __name__ == "__main__":
    game = Game()
    game.run()
