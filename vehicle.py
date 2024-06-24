class Vehicle:
    def __init__(self, color, manufacturer) -> None:
        self.is_moving = False
        self.gas_level = 50 #fake full take
        self.color = color
        self.manufacturer = manufacturer
    
    def drive(self):
        if self.gas_level > 0:
            self.gas_level -= 2
            print(f"You are driving the car, {self.color} {self.manufacturer} goes VROOOM!.")
        else:
            print(f"The {self.color} {self.manufacturer} is out of petrol.")

# Inheritance helps you NOT have to initialize again 
class Car(Vehicle):
    def window(self):
        print("Mhmmm, ahhh... fresh air. :)")