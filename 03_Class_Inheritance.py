from vehicle import Car

vrr_pha = Car("white", "VW Polo")

vrr_pha.drive()
vrr_pha.window()

distance_home = 500
# distance_home = 50
distance_covered = 0
for _ in range(distance_home + 1):
    if vrr_pha.gas_level > 0:
        vrr_pha.drive()
        distance_covered += 10

        print(f"Distance covered: {distance_covered} km, Gas level: {vrr_pha.gas_level}")

        if distance_covered >= distance_home:
            print("You had enough petrol to take you home.")
            break
        else:
            pass
    else:
        print(f"Out of petrol at {distance_covered} km, please refill your tank.")
        break
