class Line:
    def __init__(self, name, origin, destination, stations):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.stations = stations

    def __str__(self):
        return f"Line: {self.name} | {self.origin} -> {self.destination} | Stations({len(self.stations)}): {', '.join(self.stations)}"
        

class Train:
    def __init__(self, train_id, route, average_speed, stoppage, quality_level, price, capacity):
        self.train_id = train_id
        self.route = route
        self.average_speed = average_speed
        self.stoppage = stoppage
        self.quality_level = quality_level
        self.price = price
        self.capacity = capacity




        