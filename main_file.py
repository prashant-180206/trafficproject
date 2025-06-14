import pygame
from traffic_management import *
from collision_control import *
from change_direction import *
from Main_Logic import *
from image_processing import *
from arduino_control import *
from constants import *
from vehicle_management import *
from screen_control import *

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
    'is_cycle_updated': False,
    'cycle_logged': False
}

def varexchange():
    global cp1, cp2, cp3, cp4, count, check, cyclecounter, first_signal, traffic_state, max_vehicles, vehicle_moved

    vehicle_counts = {
        'north': sum(len(lane) for lane in vehiclesN),
        'east': sum(len(lane) for lane in vehiclesE),
        'west': sum(len(lane) for lane in vehiclesW),
        'south': sum(len(lane) for lane in vehiclesS)
    }

    is_cycle_start = (cyclecounter == 1)
    if not hasattr(varexchange, 'max_vehicles'):
        varexchange.max_vehicles = send_vehicle_numbers()

    if is_cycle_start or count == 0:
        varexchange.max_vehicles = send_vehicle_numbers()

    SPAWN_INTERVAL = FPS * 4
    if count == 0 or count % SPAWN_INTERVAL == 0:
        addvehicles(count, varexchange.max_vehicles, vehicle_counts['north'], vehicle_counts['east'],
                    vehicle_counts['west'], vehicle_counts['south'])

    if is_cycle_start:
        new_timings, display_info, new_first_signal = mainLogic(
            vehicle_counts['north'], vehicle_counts['east'],
            vehicle_counts['west'], vehicle_counts['south']
        )

        traffic_state['current_timings'] = new_timings
        traffic_state['first_signal'] = new_first_signal
        traffic_state['is_cycle_updated'] = True
        traffic_state['display_info'] = display_info

        cp1, cp2, cp3, cp4 = new_timings

        # Cycle is completed (all signals have been processed)
        if cyclecounter == 1 and count > FPS:
            if not traffic_state.get('cycle_logged'):
                print(f"Debug - Count: {count}, FPS: {FPS}, Cycle: {count//FPS}")
                print(f"Debug - Vehicles moved: {vehicle_moved}")
                print(f"Debug - Max vehicles: {varexchange.max_vehicles}")

                with open('result.txt', 'a') as f:
                    f.write(f"Cycle {count//FPS}:\n")
                    f.write(f"Input - Max vehicles [N,E,W,S]: {varexchange.max_vehicles}\n")
                    f.write(f"Output - Vehicles moved: {vehicle_moved}\n")
                    f.write("-" * 40 + "\n")

                traffic_state['cycle_logged'] = True
                vehicle_moved = 0
        else:
            traffic_state['cycle_logged'] = False

    else:
        traffic_state['is_cycle_updated'] = False

    if 'display_info' in traffic_state:
        display_algorithm_info(traffic_state['display_info'])

    current_timings = traffic_state['current_timings'] or [cp1, cp2, cp3, cp4]
    check, cyclecounter = manage_traffic(
        signalW, signalE, signalN, signalS,
        count, FPS, check,
        current_timings,
        traffic_state['first_signal'],
        cyclecounter
    )

    return traffic_state['first_signal']

# Main loop
cyclecounter = 1
first_signal = "North"
cp1, cp2, cp3, cp4 = 10, 10, 10, 10  # Initial timing values
max_vehicles = send_vehicle_numbers()  # Initialize max_vehicles

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screensadd(vehicle_moved)

    # Vehicle management
    vehiclesstop(vehiclesW, vehiclesE, vehiclesN, vehiclesS,
                 signalW, HEIGHT, WIDTH, roadwidth,
                 heightvehicle, widthvehicle)
    vehiclesmove()

    # Update vehicle_moved with the return value from changedir
    moved_this_frame = changedir(vehiclesW, vehiclesE, vehiclesN, vehiclesS,
                                 HEIGHT, WIDTH, roadwidth,
                                 heightvehicle, widthvehicle,
                                 vehicle_moved)
    vehicle_moved += moved_this_frame

    first_signal = varexchange()

    arduino_control(count, FPS, [signalN, signalE, signalW, signalS])

    clock.tick(FPS * rate)
    pygame.display.flip()

    count += 1

# Close Arduino connection when done
close_arduino()