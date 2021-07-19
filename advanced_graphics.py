import arcade
import math
import random


class Window(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Advanced Graphics", fullscreen=True)
        self.set_mouse_visible(False)
        self.x = 100
        self.y = 100
        self.image = arcade.load_texture(":resources:images/enemies/slimeBlock.png")
        self.gem_image = arcade.load_texture(":resources:images/items/gemYellow.png")
        self.gem_x = []
        self.gem_y = []
        for i in range(10):
            self.gem_x.append(random.randint(50, 1500))
            self.gem_y.append(random.randint(50, 850))
    
    def on_draw(self):
        arcade.start_render()
        # Draw slime character
        arcade.draw_texture_rectangle(self.x, self.y, self.image.width, self.image.height, self.image)
        # Draw gem
        for i in range(len(self.gem_x)):
            x = self.gem_x[i]
            y = self.gem_y[i]
            arcade.draw_texture_rectangle(x, y, self.gem_image.width, self.gem_image.height, self.gem_image)

    def on_update(self, deltatime):
        for i in range(len(self.gem_x)):
            x = self.gem_x[i]
            y = self.gem_y[i]
            # Check distance between character and gem
            distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
            # When too close/collected
            if distance < 75:
                self.gem_x[i] = random.randint(50, 1550)
                self.gem_y[i] = random.randint(50, 850)
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        

Window()
arcade.run()
