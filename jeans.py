class Jeans:
    # You need to have self which suggests that you're passing a refence to the object itself
    # Details are encapsulated inside an object
    def __init__(self, waist, length, colour) -> None:
        self.wearing = False
        self.clean = True
        self.waist = waist
        self.length = length
        self.colour = colour

    def put_on(self):
        print(f'Putting on my {self.waist}x{self.length} {self.colour} jeans.')
        self.wearing = True
    
    def take_off(self):
        print(f'Taking off my {self.waist}x{self.length} {self.colour} jeans.')
        self.wearing = False
    
    def dye(self, colour):
        print(f"Dyeing my jeans {colour}")
        self.colour =colour
    
    def make_clean(self):
        self.clean = True
    
    def make_dirty(self):
        self.clean = False