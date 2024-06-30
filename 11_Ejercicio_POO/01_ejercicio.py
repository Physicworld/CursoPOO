import random
import pygame

class Vehicle:
    def __init__(self, colour = "red", x=400, y=400):
        self.img_path = "../resources/sedan_" + colour + ".png"
        self.location = x, y
        self.draw()

    def draw(self):
        self.img = pygame.image.load(self.img_path)
        self.img_location = self.img.get_rect()
        self.img_location.center = self.location

class Truck(Vehicle):
    def __init__(self, x, y, type):
        super().__init__()
        self.img_path = "../resources/truck_" + type + ".png"
        self.location = x, y
        self.draw()

class F1Vehicle(Vehicle):
    def __init__(self, x, y):
        super().__init__()
        self.img_path = '../resources/F1.png'
        self.location = x, y
        self.draw()
        

def main():
    HEIGHT = 800
    WIDTH = 800
    running = True
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT, WIDTH))

    n_cars = 10
    cars = []

    for i in range(n_cars):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        vehicle_class = random.choice(['sedan', 'truck', 'f1'])

        if vehicle_class == 'sedan':
            colour = random.choice(['black', 'red', 'yellow'])
            cars.append(Vehicle(colour=colour, x=x, y=y))

        elif vehicle_class == 'truck':
            type = random.choice(['box', 'trailer'])
            cars.append(Truck(x=x, y=y, type=type))

        elif vehicle_class == 'f1':
            cars.append(F1Vehicle(x, y))

        else:
            raise "Vehicle not defined!"


    screen.fill("white")

    for car in cars:
        screen.blit(car.img, car.location)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()