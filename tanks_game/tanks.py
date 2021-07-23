import arcade
import math


class Player(arcade.Sprite):
    # Class for the player controlled tank
    def __init__(self, x, y):
        super().__init__("images/hq/tankBody_blue.png")
        self.texture_transform = arcade.Matrix3x3().rotate(90)
        self.position = x, y
        self.speed = 0

        self.barrel = arcade.Sprite("images/hq/tankBlue_barrel1.png")
        self.barrel.position = self.position


    def update(self, mouse_x, mouse_y):
        # Update the player and the barrel, then move the player, and using
        # the mouse coordinates, update the barrel rotation
        super().update()
        self.barrel.update()
        self.move()
        self.calculate_barrel_rotation(mouse_x, mouse_y)

    
    def draw(self):
        # Draw the player and the barrel
        super().draw()
        self.barrel.draw()


    def move(self):
        # Reset old speed to 0, and then move
        self.change_x = 0
        self.change_y = 0
        self.forward(self.speed)
    

    def calculate_barrel_rotation(self, mouse_x, mouse_y):
        # Trigonometric functions to calculate the angle between the player and the mouse
        adjacent = mouse_x - self.center_x
        opposite = mouse_y - self.center_y
        if adjacent == 0:
            # If the mouse is perfectly inline with the player on the y-axis, prevent a
            # zero-division error
            angle = 90 * 1 if opposite > 0 else -1
        else:
            angle = math.degrees(math.atan(opposite / adjacent))
        
        # Offset for rotations less than 0, ie. when the mouse is to the left of the player
        if adjacent < 0:
            angle += 180
        # Calculate the position for the barrel, so that it spins around its end as the mouse moves
        self.barrel.center_x = self.center_x + math.cos(math.radians(angle)) * self.barrel.height / 2
        self.barrel.center_y = self.center_y + math.sin(math.radians(angle)) * self.barrel.height / 2

        # 90 degree offset because arcade considers 0 degrees to be pointing to the right,
        # but the image of the barrel points up
        self.barrel.angle = angle + 90
    

    def fire_shot(self):
        # Create a new bullet, calculate the position of the end of the barrel
        projectile = arcade.Sprite("images/hq/bulletBlue2.png")
        barrel_angle = self.barrel.angle - 90
        barrel_end_x = self.center_x + math.cos(math.radians(barrel_angle)) * self.barrel.height
        barrel_end_y = self.center_y + math.sin(math.radians(barrel_angle)) * self.barrel.height

        # Set the bullet properties
        projectile.position = barrel_end_x, barrel_end_y
        projectile.angle = barrel_angle
        projectile.forward(10)
        # Visually point the bullet in the direction it is moving.
        projectile.angle = barrel_angle - 90
        return projectile



class Window(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Tanks Game", fullscreen=True)
        arcade.set_background_color(arcade.color.WHITE)
        # Load the map from the external file, and process the background layer
        self.map = arcade.tilemap.read_tmx("map1.tmx")
        self.background = arcade.tilemap.process_layer(self.map, "background")

        self.player = Player(self.width / 2, self.height / 2)
        self.projectiles = arcade.SpriteList()
    
        self.mouse_x = 0
        self.mouse_y = 0

        self.camera = 200, 200, self.width - 200, self.height - 200


    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.player.draw()
        self.projectiles.draw()
    

    def on_update(self, delta_time):
        self.player.update(self.mouse_x, self.mouse_y)
        self.projectiles.update()

        # Find any projectiles that have left the screen, and delete them
        for projectile in self.projectiles:
            if (
                projectile.left > self.width or projectile.right < 0 or
                projectile.top < 0 or projectile.bottom > self.height
            ):
                projectile.kill()
        
        c_left, c_right, c_top, c_bottom = self.get_viewport()



    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        
        if symbol == arcade.key.A:
            self.player.change_angle = 2
        if symbol == arcade.key.D:
            self.player.change_angle = -2
        if symbol == arcade.key.W:
            self.player.speed = 4
        if symbol == arcade.key.S:
            self.player.speed = -2


    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.A:
            self.player.change_angle = 0
        elif symbol == arcade.key.D:
            self.player.change_angle = 0
        elif symbol == arcade.key.W:
            self.player.speed = 0
        if symbol == arcade.key.S:
            self.player.speed = 0


    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y
    

    def on_mouse_press(self, x, y, button, modifiers):
        shot = self.player.fire_shot()
        self.projectiles.append(shot)



Window()
arcade.run()
