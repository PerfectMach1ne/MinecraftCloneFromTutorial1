import pyglet

# It causes problems on MacOS if enabled
pyglet.options["shadow_window"] = False
# Tanks performance if enabled
pyglet.options["debug_gl"] = False

import pyglet.gl as gl


class Window(pyglet.window.Window):
    def __init__(self, **args):
        super(Window, self).__init__(**args)

    # Called when screen is updated(?)
    def on_draw(self):
        gl.glClearColor(1.0, 0.5, 1.0, 1.0)
        self.clear()

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
