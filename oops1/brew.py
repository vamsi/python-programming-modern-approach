class Coffee():
    coffes = 0

    def __init__(self, name="Coffee", shot=1, milk=1, sugar=2, decaf=False):
        self.name = name
        self.milk = milk
        self.decaf = decaf
        self.sugar = sugar
        self.shot = shot
        self.calories = self.calculate_calories()

    def add_milk(self):
        """
        Adds milk to the brew.
        """
        self.milk += 100
        return

    def add_sugar(self):
        """
        Adds sugar to the brew.

        """
        self.sugar += 3
        return

    def describe(self):
        """
        Describes the brew.
        """
        print("{}, {}, {}, {}, {}".format(
            self.name, self.shot, self.sugar, self.decaf, self.calories))

    def calculate_calories(self):
        """
        Calculates the calories of the brewed coffee.
        """
        milk = 103
        sugar = 11
        shot = 1.8
        return (milk * self.milk + sugar * self.sugar + shot * self.shot)


c1 = Coffee(shot=2, sugar=2)
c1.describe()
