# Add global variables at module level
phasecounter = 1
cycle_completed = False

# Global state for traffic management
traffic_cycle = {
    'signal_order': None,
    'phase_lengths': None,
    'current_first_signal': None
}


def move(active_signal, other_signals):
    """
    Turn the given signal GREEN and all other signals RED.
    """
    active_signal.change_state("GREEN")
    for signal in other_signals:
        signal.change_state("RED")


def rest(*signals):
    """
    Turn all given signals RED.
    """
    for signal in signals:
        signal.change_state("RED")


def manage_traffic(signalW, signalE, signalN, signalS, count, FPS, check, phase_lengths, first_signal, cyclecounter=1):
    """
    Manage traffic signals in a cycle.
    Args:
        signals: Traffic signal objects for each direction
        phase_lengths: Timings for [North, East, West, South]
        first_signal: Direction to start the cycle ("North", "East", etc.)
    """
    STEADY_RED_DURATION = 3

    # Initialize or update signal order based on first_signal
    if traffic_cycle['signal_order'] is None or (first_signal != traffic_cycle['current_first_signal'] and cyclecounter == 1):
        # Update signal order and phase timings based on starting direction
        if first_signal == "North":
            traffic_cycle['signal_order'] = [
                signalN, signalE, signalS, signalW]
            traffic_cycle['phase_lengths'] = [phase_lengths[0], phase_lengths[1],
                                              phase_lengths[3], phase_lengths[2]]
        elif first_signal == "East":
            traffic_cycle['signal_order'] = [
                signalE, signalS, signalW, signalN]
            traffic_cycle['phase_lengths'] = [phase_lengths[1], phase_lengths[3],
                                              phase_lengths[2], phase_lengths[0]]
        elif first_signal == "South":
            traffic_cycle['signal_order'] = [
                signalS, signalW, signalN, signalE]
            traffic_cycle['phase_lengths'] = [phase_lengths[3], phase_lengths[2],
                                              phase_lengths[0], phase_lengths[1]]
        elif first_signal == "West":
            traffic_cycle['signal_order'] = [
                signalW, signalN, signalE, signalS]
            traffic_cycle['phase_lengths'] = [phase_lengths[2], phase_lengths[0],
                                              phase_lengths[1], phase_lengths[3]]
        traffic_cycle['current_first_signal'] = first_signal

    # Calculate total cycle duration and current phase
    total_duration = sum(phase_lengths) + STEADY_RED_DURATION * 4
    phase_counter = (count // FPS) % total_duration

    # Calculate phase transition times
    t1 = phase_lengths[0]                                  # First green ends
    t2 = t1 + STEADY_RED_DURATION                         # First red ends
    t3 = t2 + phase_lengths[1]                            # Second green ends
    t4 = t3 + STEADY_RED_DURATION                         # Second red ends
    t5 = t4 + phase_lengths[2]                            # Third green ends
    t6 = t5 + STEADY_RED_DURATION                         # Third red ends
    t7 = t6 + phase_lengths[3]                            # Fourth green ends

    # Debug prints


    # Execute appropriate signal phase
    if phase_counter < t1:  # First green phase
        move(traffic_cycle['signal_order'][0],
             [s for s in traffic_cycle['signal_order'] if s != traffic_cycle['signal_order'][0]])
        cyclecounter = 0
    elif phase_counter < t2:  # First steady red
        rest(signalW, signalE, signalN, signalS)
    elif phase_counter < t3:  # Second green phase
        move(traffic_cycle['signal_order'][1],
             [s for s in traffic_cycle['signal_order'] if s != traffic_cycle['signal_order'][1]])
    elif phase_counter < t4:  # Second steady red
        rest(signalW, signalE, signalN, signalS)
    elif phase_counter < t5:  # Third green phase
        move(traffic_cycle['signal_order'][2],
             [s for s in traffic_cycle['signal_order'] if s != traffic_cycle['signal_order'][2]])
    elif phase_counter < t6:  # Third steady red
        rest(signalW, signalE, signalN, signalS)
    elif phase_counter < t7:  # Fourth green phase
        move(traffic_cycle['signal_order'][3],
             [s for s in traffic_cycle['signal_order'] if s != traffic_cycle['signal_order'][3]])
        cyclecounter = 1  # Prepare for next cycle
    else:  # Final steady red
        rest(signalW, signalE, signalN, signalS)

    return phase_counter, cyclecounter
