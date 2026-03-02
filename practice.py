class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_coordinates(self):
        for value in range(self.x, self.y):
            self.x = value
            self.y = value
            print(f"({self.x}, {self.y})")

coordinate = Coordinate(0, 11)
coordinate.show_coordinates()