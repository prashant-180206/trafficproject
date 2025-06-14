def backup_algorithm(north_length, east_length, west_length, south_length):
    # Simple round-robin algorithm as a fallback
    timings = [10, 10, 10, 10]
    algorithm_used = "Backup Algorithm (Round-Robin)"
    return timings, algorithm_used

def mainLogic(north_length, east_length, west_length, south_length):
    try:
        # Define thresholds for high and low density
        DENSITY_THRESHOLD = 8

        # Calculate average density
        total_vehicles = north_length + east_length + west_length + south_length
        average_density = total_vehicles / 4

        # Initialize phase timings
        phase1count = 10  # Default time for North
        phase2count = 10  # Default time for East
        phase3count = 10  # Default time for South
        phase4count = 10  # Default time for West

        # Dynamic timing based on vehicle count for each lane
        def get_dynamic_time(vehicle_count):
            if vehicle_count < 5:
                return 10  # Fixed 10 seconds for less than 5 vehicles
            elif 5 <= vehicle_count < 10:
                return 15  # 15 seconds for 5-9 vehicles
            elif 10 <= vehicle_count < 15:
                return 20  # 20 seconds for 10-14 vehicles
            else:
                return 25  # 25 seconds for 15+ vehicles

        # Determine which algorithm to use based on average density
        if average_density > DENSITY_THRESHOLD:
            algorithm_used = "High-Density Algorithm"
            # Prioritize the lane with the highest density
            max_density = max(north_length, east_length, south_length, west_length)
            if max_density == north_length:
                phase1count = 20  # North gets more time
                phase2count = get_dynamic_time(east_length)
                phase3count = get_dynamic_time(south_length)
                phase4count = get_dynamic_time(west_length)
                first_signal = "North"
            elif max_density == east_length:
                phase1count = get_dynamic_time(north_length)
                phase2count = 20  # East gets more time
                phase3count = get_dynamic_time(south_length)
                phase4count = get_dynamic_time(west_length)
                first_signal = "East"
            elif max_density == south_length:
                phase1count = get_dynamic_time(north_length)
                phase2count = get_dynamic_time(east_length)
                phase3count = 20  # South gets more time
                phase4count = get_dynamic_time(west_length)
                first_signal = "South"
            else:
                phase1count = get_dynamic_time(north_length)
                phase2count = get_dynamic_time(east_length)
                phase3count = get_dynamic_time(south_length)
                phase4count = 20  # West gets more time
                first_signal = "West"

        elif average_density < DENSITY_THRESHOLD:
            algorithm_used = "Low-Density Algorithm"
            # Prioritize the lane with the lowest density
            min_density = min(north_length, east_length, south_length, west_length)
            if min_density == north_length:
                phase1count = 10  # North gets more time
                phase2count = get_dynamic_time(east_length)
                phase3count = get_dynamic_time(south_length)
                phase4count = get_dynamic_time(west_length)
                first_signal = "North"
            elif min_density == east_length:
                phase1count = get_dynamic_time(north_length)
                phase2count = 10  # East gets more time
                phase3count = get_dynamic_time(south_length)
                phase4count = get_dynamic_time(west_length)
                first_signal = "East"
            elif min_density == south_length:
                phase1count = get_dynamic_time(north_length)
                phase2count = get_dynamic_time(east_length)
                phase3count = 10  # South gets more time
                phase4count = get_dynamic_time(west_length)
                first_signal = "South"
            else:
                phase1count = get_dynamic_time(north_length)
                phase2count = get_dynamic_time(east_length)
                phase3count = get_dynamic_time(south_length)
                phase4count = 10  # West gets more time
                first_signal = "West"

        else:
            algorithm_used = "Default Algorithm"
            first_signal = "North"  # Default to North if densities are equal
            # Use dynamic timing for all phases
            phase1count = get_dynamic_time(north_length)
            phase2count = get_dynamic_time(east_length)
            phase3count = get_dynamic_time(south_length)
            phase4count = get_dynamic_time(west_length)

        # Skip lanes with 0 vehicles
        if north_length == 0:
            phase1count = 0
        if east_length == 0:
            phase2count = 0
        if south_length == 0:
            phase3count = 0
        if west_length == 0:
            phase4count = 0

        # Prepare display information
        display_info = {
            "algorithm_used": algorithm_used,
            "average_density": average_density,
            "north_vehicles": north_length,
            "east_vehicles": east_length,
            "south_vehicles": south_length,
            "west_vehicles": west_length,
            "north_time": phase1count,
            "east_time": phase2count,
            "south_time": phase3count,
            "west_time": phase4count,
        }

        return [phase1count, phase2count, phase3count, phase4count], display_info, first_signal

    except Exception as e:
        print(f"Error in mainLogic: {e}. Falling back to backup algorithm.")
        return backup_algorithm(north_length, east_length, west_length, south_length)