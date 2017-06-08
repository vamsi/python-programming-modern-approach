class Box:

    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

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

    def compare(self, other_box):
        volume1 = self.volume()
        volume2 = other_box.volume()
        difference_volume = volume1 - volume2
        if difference_volume > 0:
            print("{} bigger than {}". format(self, other_box))
        else:
            print("{} bigger than {}". format(other_box, self))


b1 = Box(2, 3, 5)
b1.describe()
b1.reset()
b2 = Box(7, 8, 1)
b2.describe()
b3 = Box(8, 2, 7)
b3.describe()
b3.reset()
b3.describe()

Box.compare(b1, b2)
b1.compare(b2)
