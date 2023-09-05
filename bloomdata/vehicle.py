'''
This file holds two classes: Vehicle and Convertible.
They are a parent and child class.
Imagine I want to list theses vehicles on Craigslist
"Parent" class is the more the generic of the two
'''


class Vehicle:
    '''
    This is the class docstring
    '''
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        return "Hoooooooooooooonk"

    def drive(self, miles_driven):
        self.mileage += miles_driven
        return self.mileage

    def __repr__(self):
        return f'''A {self.color} {self.make}
                     {self.model} with {self.mileage} miles.'''


if __name__ == '__main__':
    my_vehicle = Vehicle('Toyota', 'Corolla', 'Gray', 2019, 64000)

# Imagine I want to list these vehicles on Craigslist
# The more specific class is called the "child" class
# Convertible inherits from vehicle


class Convertible(Vehicle):
    '''
    This is the class docstring
    '''
    def __init__(self, make, model, year, mileage,
                 color='black', top_down=True):
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return "Top is now up!"
        else:
            self.top_down = True
            return "Top is now down!"

    def __repr__(self):
        return f'''A {self.color} {self.make}
                     {self.model} convertible with {self.mileage} miles'''


if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Corolla', 'Gray', 2019, 64000)
    print(my_vehicle.honk())
    print(my_vehicle.drive(2000))
