import tkinter as tk
import random
import logging
import math

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

class Fish:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.size = 20
        self.radius = self.size / 2
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-5, 5)
        self.fish_id = self.canvas.create_oval(
            self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color
        )

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.canvas.move(self.fish_id, self.speed_x, self.speed_y)

        # Boundary checking and bounce back
        if self.x <= 0 or self.x + self.size >= self.canvas.winfo_width():
            self.speed_x = -self.speed_x
        if self.y <= 0 or self.y + self.size >= self.canvas.winfo_height():
            self.speed_y = -self.speed_y

    def change_direction_and_speed(self):
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)

    def grow_fish(self):
        self.size += 3
        self.radius = self.size / 2
        self.canvas.coords(self.fish_id, self.x, self.y, self.x + self.size, self.y + self.size)

class AquariumApp:
    def __init__(self, parent):
        self.canvas = tk.Canvas(parent, width=800, height=600, bg='lightblue')
        self.canvas.pack()
        self.fish_list = []
        self.animate()

    def add_fish(self):
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        color = self.random_color()
        new_fish = Fish(self.canvas, x, y, color)
        self.fish_list.append(new_fish)
        logging.debug(f"Fish added at ({x}, {y}) with color {color}")

    def check_collisions(self):
        for i, fish1 in enumerate(self.fish_list):
            for j, fish2 in enumerate(self.fish_list):
                if i != j:
                    dx = (fish1.x + fish1.radius) - (fish2.x + fish2.radius)
                    dy = (fish1.y + fish1.radius) - (fish2.y + fish2.radius)
                    distance = math.sqrt(dx ** 2 + dy ** 2)
                    if distance < fish1.radius + fish2.radius:
                        chosen_fish = random.choice([fish1, fish2])
                        chosen_fish.change_direction_and_speed()
                        logging.debug(f"Collision detected: {fish1} and {fish2}. Changed direction of {chosen_fish}")

    def animate(self):
        for fish in self.fish_list:
            fish.move()
        self.check_collisions()
        self.canvas.after(50, self.animate)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def grow_all_fish(self):
        for fish in self.fish_list:
            fish.grow_fish()