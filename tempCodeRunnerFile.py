import pygame
from traffic_management import *
from collision_control import *
from change_direction import *
from Main_Logic import *
from image_processing import *
from arduino_control import *
from constants import *
from vehicle_management import *
from screen_control import screensadd, display_algorithm_info

# Initialize Pygame
setup_arduino()
pygame.init()

# Set up screen
pygame.display.set_caption("Traffic Simulator")
pygame.time.wait(2000)

# Initialize clock and game state variables
clock = pygame.time.Clock()

# Global state variables
traffic_state = {
    'first_signal': "North",
    'prev_cycle_count': 0,
    'current_timings': None,