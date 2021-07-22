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
        for i in range(0):
            self.gem_x.append(random.randint(50, 1500))
            self.gem_y.append(random.randint(50, 850))

        self.numbers = []
        for i in range(10):
            image_name = "numbers/" + str(i) + ".png"
            number = arcade.Sprite(image_name, 4)
            number.alpha = 70
            self.numbers.append(number)
        
        # Amount of time game has been running
        self.time = 0
        self.score = 0

        self.gems_created = 0


    def get_numbers(self, value):
        """ Converts an integer input to a series of number sprites.
        """
        last = 0
        # Split the value into digits
        as_string = str(value)

        for i in range(len(as_string)):
            # Get each digit
            digit = int(as_string[i])

            # Get number images for each digit
            number = self.numbers[digit]
            number.left = last
            number.bottom = 0
            last = number.right

            # Draw the number images
            number.draw()


    
    def on_draw(self):
        arcade.start_render()

        # Draw slime character
        arcade.draw_texture_rectangle(self.x, self.y, self.image.width, self.image.height, self.image)
        # Draw gem
        for i in range(len(self.gem_x)):
            x = self.gem_x[i]
            y = self.gem_y[i]
            arcade.draw_texture_rectangle(x, y, self.gem_image.width, self.gem_image.height, self.gem_image)
        
        self.get_numbers(self.score)
        


    def on_update(self, deltatime):
        self.time = self.time + deltatime
        
        # Check if enough time has passed to create a new gem
        if self.time > self.gems_created * 2:
            self.gem_x.append(random.randint(50, 1500))
            self.gem_y.append(random.randint(50, 850))
            self.gems_created = self.gems_created + 1

        # Loop through all gems, check distance between gem and the player
        for i in range(len(self.gem_x)):
            x = self.gem_x[i]
            y = self.gem_y[i]
            # Check distance between character and gem
            distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
            # When too close/collected
            if distance < 75:
                self.gem_x[i] = random.randint(50, 1550)
                self.gem_y[i] = random.randint(50, 850)
                self.score = self.score + 1
    

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y
    
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        

Window()
arcade.run()
