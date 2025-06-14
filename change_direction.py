def changedir(vehiclesW, vehiclesE, vehiclesN, vehiclesS, HEIGHT, WIDTH, roadwidth, heightvehicle, widthvehicle, vehicles_moved):
    moved_count = 0  # Local counter for this frame

    # for vehicles to move at their own left side
    for vehicle in vehiclesE[0]:
        if vehicle.posx < (WIDTH//2+roadwidth//2-30) and vehicle.directiony == 0:
            temp = vehicle.height
            vehicle.height = vehicle.width
            vehicle.width = temp
            vehicle.directionx = 0
            vehicle.directiony = 5
            moved_count += 1

    for vehicle in vehiclesW[0]:
        if vehicle.posx+heightvehicle > (WIDTH//2-roadwidth//2+30) and vehicle.directiony == 0:
            temp = vehicle.height
            vehicle.height = vehicle.width
            vehicle.width = temp
            vehicle.directionx = 0
            vehicle.directiony = -5
            moved_count += 1

    for vehicle in vehiclesN[0]:
        if vehicle.posy+heightvehicle > (HEIGHT//2-roadwidth//2+30) and vehicle.directionx == 0:
            temp = vehicle.height
            vehicle.height = vehicle.width
            vehicle.width = temp
            vehicle.directionx = 5
            vehicle.directiony = 0
            moved_count += 1

    for vehicle in vehiclesS[0]:
        if vehicle.posy < (HEIGHT//2+roadwidth//2-30) and vehicle.directionx == 0:
            temp = vehicle.height
            vehicle.height = vehicle.width
            vehicle.width = temp
            vehicle.directionx = -5
            vehicle.directiony = 0
            moved_count += 1

    # for vehicles to move at their own right side
    for vehicle in vehiclesE[2]:
        if vehicle.posx < (WIDTH//2-30) and vehicle.directiony == 0:
            temp = vehicle.height
            vehicle.height = vehicle.width
            vehicle.width = temp
            vehicle.directionx = 0
            vehicle.directiony = -5
            moved_count += 3
    for vehicle in vehiclesW[2]:
        if vehicle.posx+heightvehicle > (WIDTH//2+30) and vehicle.directiony == 0:
            temp = vehicle.height
            vehicle.height = vehicle.width
            vehicle.width = temp
            vehicle.directionx = 0
            vehicle.directiony = 5
            moved_count += 3

    for vehicle in vehiclesN[2]:
        if vehicle.posy+heightvehicle > (HEIGHT//2+40) and vehicle.directionx == 0:
            temp = vehicle.height
            vehicle.height = vehicle.width
            vehicle.width = temp
            vehicle.directionx = -5
            vehicle.directiony = 0
            moved_count += 3

    for vehicle in vehiclesS[2]:
        if vehicle.posy < (HEIGHT//2-40) and vehicle.directionx == 0:
            temp = vehicle.height
            vehicle.height = vehicle.width
            vehicle.width = temp
            vehicle.directionx = 5
            vehicle.directiony = 0
            moved_count += 3

    return moved_count  # Return the number of vehicles that changed direction this frame
