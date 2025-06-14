import pygame
import random

# Screen and display settings
WIDTH, HEIGHT = 1200, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game settings
rate = 1
FPS = 40
check = 1
vehicle_moved = 0
count = 1

# Road and vehicle dimensions
roadwidth = 250
widthvehicle = 60
heightvehicle = 30

# Vehicle lists (initialize empty)
vehiclesE = [[], [], []]
vehiclesW = [[], [], []]
vehiclesN = [[], [], []]
vehiclesS = [[], [], []]

# Colors
GRAY = (169, 169, 169)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MIDNIGHT_BLUE = (25, 25, 112)
CRIMSON_RED = (120, 20, 60)
FOREST_GREEN = (34, 139, 34)
SUNBURST_ORANGE = (255, 69, 0)

# Classes


class randfun:
    @staticmethod
    def getVehicleHeight():
        return random.choice([20, 25, 30])

    @staticmethod
    def getVehicleWidth():
        return random.choice([40, 50, 60])


class TrafficSignal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "GREEN"

    def change_state(self, state):
        self.state = state

    def draw(self):
        color = GREEN if self.state == "GREEN" else RED
        pygame.draw.circle(screen, color, (self.x, self.y), 15)


class Vehicle:
    def __init__(self, posx, posy, width, height, directionx=0, directiony=0):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.directionx = directionx
        self.directiony = directiony
        self.speed = random.randint(2, 5)
        self.colors = [MIDNIGHT_BLUE, CRIMSON_RED,
                       FOREST_GREEN, SUNBURST_ORANGE]
        self.color = random.choice(self.colors)

    def stop(self):
        self.posx -= self.directionx
        self.posy -= self.directiony

    def move(self):
        self.posx += self.directionx
        self.posy += self.directiony

    def draw(self):
        pygame.draw.rect(
            screen,
            self.color,
            (self.posx, self.posy, self.width, self.height),
            border_radius=10,
        )


# Initialize signals
signalW = TrafficSignal(WIDTH // 2 - roadwidth // 2, HEIGHT // 2)
signalE = TrafficSignal(WIDTH // 2 + roadwidth // 2, HEIGHT // 2)
signalN = TrafficSignal(WIDTH // 2, HEIGHT // 2 - roadwidth // 2)
signalS = TrafficSignal(WIDTH // 2, HEIGHT // 2 + roadwidth // 2)
