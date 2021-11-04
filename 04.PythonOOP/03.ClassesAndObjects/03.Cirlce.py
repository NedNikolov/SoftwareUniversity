class Circle:
    # class attribute, class variable
    pi = 3.14

    def __init__(self, radius):
        # object attribute, instance attribute, instance variable
        self.radius = radius

    def get_area(self):
        return self.pi * self.radius ** 2

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_circumference(self):
        return 2 * self.pi * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
