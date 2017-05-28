class Box:
    def reset(self):
        self.width = 2
        self.height = 2
        self.depth = 2


b = Box()
b.reset()

print(b.height, b.width, b.depth)
