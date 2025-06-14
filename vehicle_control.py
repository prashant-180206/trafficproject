from constants import *

def create_vehicle(lane, pos_x, pos_y, width, height, dir_x, dir_y, condition):
    if condition:
        vehicle = Vehicle(pos_x, pos_y, width, height, dir_x, dir_y)
        lane.append(vehicle)


def addvehicles(count, max_vehicles, nl, el, wl, sl):
    # Vehicles moving to the left from the east
    pos_ys_east = [
        HEIGHT // 2 + (roadwidth // 2 - 10 - heightvehicle),
        HEIGHT // 2 + (roadwidth // 2 - 10 - 2 * heightvehicle - 5),
        HEIGHT // 2 + (roadwidth // 2 - 10 - 3 * heightvehicle - 10),
    ]
    dirs_east = [-3, -4, -2]
    i = 0
    while i < len(pos_ys_east):
        pos_y = pos_ys_east[i]
        dir_east = dirs_east[i]
        create_vehicle(
            vehiclesE[i],
            WIDTH + 80,
            pos_y,
            randfun.getVehicleWidth(),
            randfun.getVehicleHeight(),
            dir_east,
            0,
            el < max_vehicles[1],
        )
        i += 1

    # Vehicles moving to the right from the west
    pos_ys_west = [
        HEIGHT // 2 - roadwidth // 2 + 10,
        HEIGHT // 2 - roadwidth // 2 + 10 + heightvehicle + 5,
        HEIGHT // 2 - roadwidth // 2 + 10 + 2 * heightvehicle + 10,
    ]
    dirs_west = [3, 4, 2]
    i = 0
    while i < len(pos_ys_west):
        pos_y = pos_ys_west[i]
        dir_west = dirs_west[i]
        create_vehicle(
            vehiclesW[i],
            -80,
            pos_y,
            randfun.getVehicleWidth(),
            randfun.getVehicleHeight(),
            dir_west,
            0,
            wl < max_vehicles[2],
        )
        i += 1

    # Vehicles moving down from the north
    pos_xs_north = [
        WIDTH // 2 + roadwidth // 2 - 40,
        WIDTH // 2 + roadwidth // 2 - heightvehicle - 45,
        WIDTH // 2 + roadwidth // 2 - 2 * heightvehicle - 50,
    ]
    dirs_north = [3, 4, 2]
    i = 0
    while i < len(pos_xs_north):
        pos_x = pos_xs_north[i]
        dir_north = dirs_north[i]
        create_vehicle(
            vehiclesN[i],
            pos_x,
            -80,
            randfun.getVehicleHeight(),
            randfun.getVehicleWidth(),
            0,
            dir_north,
            nl < max_vehicles[0],
        )
        i += 1

    # Vehicles moving up from the south
    pos_xs_south = [
        WIDTH // 2 - roadwidth // 2 - 20 + heightvehicle,
        WIDTH // 2 - roadwidth // 2 - 15 + 2 * heightvehicle,
        WIDTH // 2 - roadwidth // 2 - 10 + 3 * heightvehicle,
    ]
    dirs_south = [-3, -4, -2]
    i = 0
    while i < len(pos_xs_south):
        pos_x = pos_xs_south[i]
        dir_south = dirs_south[i]
        create_vehicle(
            vehiclesS[i],
            pos_x,
            HEIGHT + 80,
            randfun.getVehicleHeight(),
            randfun.getVehicleWidth(),
            0,
            dir_south,
            sl < max_vehicles[3],
        )
        i += 1


def move_vehicles_in_lane(vehicles, signal, threshold, width_limit, height_limit, direction):
    for vehicle in vehicles:
        if signal.state == "GREEN" or direction(vehicle, threshold):
            vehicle.move()
    return [
        v
        for v in vehicles
        if -100 <= v.posx <= width_limit + 100 and -100 <= v.posy <= height_limit + 100
    ]


def vehiclesmove():
    global vehiclesW, vehiclesE, vehiclesN, vehiclesS

    def is_outside_range(position, lower_bound, upper_bound):
        return position < lower_bound or position > upper_bound

    def move_west(vehicle, threshold):
        return is_outside_range(vehicle.posx, threshold, threshold + 10)

    def move_east(vehicle, threshold):
        return is_outside_range(vehicle.posx, threshold - 10, threshold)

    def move_north(vehicle, threshold):
        return is_outside_range(vehicle.posy, threshold, threshold + 10)

    def move_south(vehicle, threshold):
        return is_outside_range(vehicle.posy, threshold - 10, threshold)

    vehiclesW = [
        move_vehicles_in_lane(
            lane,
            signalW,
            WIDTH // 2 - roadwidth // 2 - widthvehicle,
            WIDTH,
            HEIGHT,
            move_west,
        )
        for lane in vehiclesW
    ]
    vehiclesE = [
        move_vehicles_in_lane(
            lane,
            signalE,
            WIDTH // 2 + roadwidth // 2,
            WIDTH,
            HEIGHT,
            move_east
        )
        for lane in vehiclesE
    ]
    vehiclesN = [
        move_vehicles_in_lane(
            lane,
            signalN,
            HEIGHT // 2 - roadwidth // 2 - widthvehicle,
            WIDTH,
            HEIGHT,
            move_north,
        )
        for lane in vehiclesN
    ]
    vehiclesS = [
        move_vehicles_in_lane(
            lane,
            signalS,
            HEIGHT // 2 + roadwidth // 2,
            WIDTH,
            HEIGHT,
            move_south
        )
        for lane in vehiclesS
    ]

