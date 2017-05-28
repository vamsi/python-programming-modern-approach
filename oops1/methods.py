class Box:

    def reset(self):
        print("I am being reset")
        self.height = 2
        self.depth = 2
        self.width = 2
        print("Reset complete")

    def resize(self, height, width, depth):
        print("I am resizing")
        self.height = height
        self.depth = depth
        self.width = width
        return "Resize complete"

    def volume(self):
        return self.height * self.width * self.depth

    def surface_area(self):
        return 2 * (self.height + self.width *
                    self.width + self.depth *
                    self.width + self.depth)

    def describe(self):
        print("Hey, I am box! with volume {}mm, and surface area {}mm.".format(
            self.volume(),
            self.surface_area()))


b1 = Box()
b1.height, b1.width, b1.depth = 2, 3, 5
print(b1.volume())
print(b1.surface_area())
b1.describe()
b1.reset()
print(b1.volume())
b1.describe()
b1.resize(8, 2, 3)
b1.describe()
