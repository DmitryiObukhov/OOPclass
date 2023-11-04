class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        if self.speed >= 0:
            print(f"Current speed: {self.speed} km/h")
            self.speed += 7
            print(f"Accelerated speed: {self.speed} km/h")

    def brake(self):
        if self.speed > 5:
            print(f"Initial speed: {self.speed} km/h")
            self.speed -= 5
            print(f"Braked speed: {self.speed} km/h")

    def display_speed(self):
        print(f"Current speed: {self.speed} km/h")
