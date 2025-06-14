import pygame
from constants import (
    screen, WIDTH, HEIGHT, roadwidth, GRAY, BLACK, WHITE,
    vehiclesW, vehiclesE, vehiclesN, vehiclesS,
    signalW, signalE, signalN, signalS,
    vehicle_moved,
)


def screensadd(vehicle_moved):
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLACK, (0, HEIGHT // 2 -
                     roadwidth // 2, WIDTH, roadwidth))
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 -
                     roadwidth // 2, 0, roadwidth, HEIGHT))

    pygame.draw.line(screen, WHITE, (0, HEIGHT // 2),
                     (WIDTH // 2 - roadwidth // 2, HEIGHT // 2), 5)
    pygame.draw.line(screen, WHITE, (WIDTH // 2 + roadwidth //
                     2, HEIGHT // 2), (WIDTH, HEIGHT // 2), 5)
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0),
                     (WIDTH // 2, HEIGHT // 2 - roadwidth // 2), 5)
    pygame.draw.line(screen, WHITE, (WIDTH // 2, HEIGHT //
                     2 + roadwidth // 2), (WIDTH // 2, HEIGHT), 5)

    # Draw vehicles
    for lanes in [vehiclesW, vehiclesE, vehiclesN, vehiclesS]:
        for lane in lanes:
            for vehicle in lane:
                vehicle.draw()

    # Draw traffic signals
    signalW.draw()
    signalE.draw()
    signalN.draw()
    signalS.draw()

    # Draw vehicle counts
    directions = {
        "North": (WIDTH // 2, HEIGHT // 2 - roadwidth // 2 - 50),
        "South": (WIDTH // 2, HEIGHT // 2 + roadwidth // 2 + 50),
        "East": (WIDTH // 2 + roadwidth // 2 + 50, HEIGHT // 2),
        "West": (WIDTH // 2 - roadwidth // 2 - 50, HEIGHT // 2),
    }
    counts = {
        "North": sum(len(lane) for lane in vehiclesN),
        "South": sum(len(lane) for lane in vehiclesS),
        "East": sum(len(lane) for lane in vehiclesE),
        "West": sum(len(lane) for lane in vehiclesW),
    }
    font = pygame.font.Font(None, 36)

    for direction, pos in directions.items():
        pygame.draw.circle(screen, BLACK, pos, 25)
        pygame.draw.circle(screen, WHITE, pos, 23)
        text = font.render(str(counts[direction]), True, BLACK)
        screen.blit(text, text.get_rect(center=pos))

    # Draw moved vehicles count
    pygame.draw.rect(screen, WHITE, (50, 50, 250, 40))
    text = font.render(f"Moved Vehicles: {int(vehicle_moved)}", True, BLACK)
    text_rect = text.get_rect(center=(50 + 250 // 2, 50 + 40 // 2))
    screen.blit(text, text_rect)


def display_algorithm_info(display_info):
    font = pygame.font.Font(None, 24)
    x, y = WIDTH - 300, 50

    text = font.render(
        f"Algorithm: {display_info['algorithm_used']}", True, BLACK)
    screen.blit(text, (x, y))
    y += 30

    text = font.render(
        f"Avg Density: {display_info['average_density']:.2f}", True, BLACK)
    screen.blit(text, (x, y))
    y += 30

    text = font.render(
        f"North: {display_info['north_vehicles']} vehicles, Time: {display_info['north_time']}s", True, BLACK)
    screen.blit(text, (x, y))
    y += 30

    text = font.render(
        f"East: {display_info['east_vehicles']} vehicles, Time: {display_info['east_time']}s", True, BLACK)
    screen.blit(text, (x, y))
    y += 30

    text = font.render(
        f"West: {display_info['west_vehicles']} vehicles, Time: {display_info['west_time']}s", True, BLACK)
    screen.blit(text, (x, y))
    y += 30

    text = font.render(
        f"South: {display_info['south_vehicles']} vehicles, Time: {display_info['south_time']}s", True, BLACK)
    screen.blit(text, (x, y))
