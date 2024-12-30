class Car:
    def __init__(self, color, model, price):
        # attributes 
        self.color = color
        self.model = model
        self.price = price
    # methods
    def start(self):
        print(f"The {self.color} {self.model} car is starting.")

    def stop(self):
        print(f"The {self.color} {self.model} car is stopping.")

    def move_forward(self):
        print(f"The {self.color} {self.model} car is moving forward.")

    def move_backward(self):
        print(f"The {self.color} {self.model} car is moving backward.")

my_car = Car("Red", "Toyota Corolla", 20000)
if __name__ == "__main__":
    my_car.start()
    my_car.move_forward()
    my_car.move_backward()
    my_car.stop()

