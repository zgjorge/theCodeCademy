# Calculating shipping

premium_shipping = 125.00


def ground_shipping(weight):
    if weight < 2:
        return round((weight * 1.5 + 20), 2)
    elif 2 < weight <= 6:
        return round((weight * 3 + 20), 2)
    elif 6 < weight <= 10:
        return round((weight * 4 + 20), 2)
    else:
        return round((weight * 4.75 + 20), 2)


def drone_shipping(weight):
    if weight < 2:
        return round((weight * 4.50), 2)
    elif 2 < weight <= 6:
        return round((weight * 9), 2)
    elif 6 < weight <= 10:
        return round((weight * 12), 2)
    else:
        return round((weight * 14.25), 2)


def cheapest(weight):
    ground = ground_shipping(weight)
    drone = drone_shipping(weight)
    if drone > ground < premium_shipping:
        return "Ground method is the cheapest, with a total of : $" + str(ground) + " vs $" + str(drone) + " for Drone."
    elif drone < ground < premium_shipping:
        return "Drone method is the cheapest, with a total of: $" + str(drone) + " vs $" + str(ground) + " for Ground."
    else:
        return "Ground shipping is the cheapest, with a total of: $" + str(premium_shipping)


# print(ground_shipping(1))
# print(drone_shipping(1.5))
print(cheapest(2))
