class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def touches(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance <= (self.radius + other.radius)

    def overlaps(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance < (self.radius + other.radius)

# Test cases
c1 = Circle(0, 0, 5)
c2 = Circle(6, 0, 4)
c3 = Circle(20, 0, 1)

print("c1 touches c2:", c1.touches(c2))
print("c1 touches c3:", c1.touches(c3))
print("c1 overlaps c2:", c1.overlaps(c2))
print("c1 overlaps c3:", c1.overlaps(c3))