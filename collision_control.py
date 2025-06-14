def vehiclesstop(vehiclesW, vehiclesE, vehiclesN, vehiclesS, signalW,HEIGHT,WIDTH,roadwidth,heightvehicle,widthvehicle):

    for lane in vehiclesW:
        for i in range(0, len(lane)-1):  # Start from 1 to compare with the previous element
            pos1 = lane[i+1].posx
            pos2 = lane[i].posx
            if pos2 - pos1 < 75 :  # Check if distance is less than 90
                lane[i+1].stop()  # Stop vehicles if distance is less than 90
        for vehicle in lane:
            if vehicle.posx >(WIDTH//2-roadwidth//2-heightvehicle-10):
                vehicle.move()

    for lane in vehiclesE:
        for i in range(0, len(lane)-1):  # Start from 1 to compare with the previous element
            pos1 = lane[i+1].posx
            pos2 = lane[i].posx
            if pos1 - pos2 < 75 :  # Check if distance is less than 90
                lane[i+1].stop()  # Stop vehicles if distance is less than 90
        for vehicle in lane:
            if vehicle.posx <(WIDTH//2+roadwidth//2-10):
                vehicle.move()

    for lane in vehiclesN:
        for i in range(0, len(lane)-1):  # Start from 1 to compare with the previous element
            pos1 = lane[i+1].posy
            pos2 = lane[i].posy
            if pos2 - pos1 < 75 :  # Check if distance is less than 75
                lane[i+1].stop()  # Stop vehicles if distance is less than 90
        for vehicle in lane:
            if vehicle.posy >(HEIGHT//2-roadwidth//2-10-heightvehicle):
                vehicle.move()

    for lane in vehiclesS:
        for i in range(0, len(lane)-1):  # Start from 1 to compare with the previous element
            pos1 = lane[i+1].posy
            pos2 = lane[i].posy
            if pos1 - pos2 < 75 :  # Check if distance is less than 90
                lane[i+1].stop()  # Stop vehicles if distance is less than 90
        for vehicle in lane:
            if vehicle.posy <(HEIGHT//2+roadwidth//2-10):
                vehicle.move()