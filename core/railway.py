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
    def __init__(self, train_id, line_name, average_speed, stoppage, quality_level, price, capacity):
        self.train_id = train_id
        self.line_name = line_name

        self.average_speed = int(average_speed)
        self.stoppage = stoppage
        self.quality_level = quality_level

        self.price = int(price)
        self.capacity = int(capacity)
        self.remaining_capacity = int(capacity)

    def __str__(self):
        return (
            f"Train ID: {self.train_id} | Line name: {self.line_name} | Average speed: {self.average_speed} | "
            f"Stoppage: {self.stoppage} | Quality level: {self.quality_level} | Price: {self.price} | Capacity: {self.capacity} | Remaining capacity: {self.remaining_capacity}"
        )