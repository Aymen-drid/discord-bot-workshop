from module import Car
class Bicycle(Car):
    def __init__(self, color, model, price):
        super().__init__(color, model, price)  # Inherit from Vehicle
       
    def pedal(self):
        print(f"The {self.color} {self.model} bicycle with ")

# Create a Bicycle object
my_bike = Bicycle("Blue", "Mountain Bike", 300)

# Call methods from both Bicycle and Vehicle classes
my_bike.start()       # Inherited from Vehicle
my_bike.pedal()       # Method specific to Bicycle
my_bike.stop()        # Inherited from Vehicle
