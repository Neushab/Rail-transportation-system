class Line:
    def __init__(self, name, origin, destination, stations):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.stations = stations

    def __str__(self):
        return (
            f"Line: {self.name} | {self.origin} -> {self.destination} | "
            f"Stations({len(self.stations)}): {', '.join(self.stations)}"
        )


class Train:
    def __init__(self, train_id, name, line_name, speed, stoptime, level, price, capacity):
        self.train_id = train_id
        self.name = name
        self.line_name = line_name

        self.speed = int(speed)
        self.stoptime = stoptime
        self.level = level

        self.price = int(price)
        self.capacity = int(capacity)
        self.remaining_capacity = int(capacity)

    def __str__(self):
        return (
            f"ID:{self.train_id} | Train:{self.name} | Line:{self.line_name} | "
            f"Price:{self.price} | Remaining:{self.remaining_capacity}"
        )