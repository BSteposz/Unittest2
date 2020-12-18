
class Car(object):
    """ Random class car"""
    def __init__(self, speed=0):
        """ Initialize default speed, distance and time """
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        """ Print current speed in km/k"""
        print(f"I'm going {self.speed} km/h")

    def accelerate(self):
        """ Add more speed! """
        self.speed += 5

    def brake(self):
        """ Subtract spedd """
        self.speed -= 5

    def step(self):

        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        """ Calculate avarge speed"""
        return self.odometer / self.time


if __name__ == '__main__':

    my_car = Car()

    while True:
        action = input("Press: "
                       "[A}ccelerate, ""[B]rake, show [O]dometer, ""or show average [S]peed").upper()

        if action not in "ABOS" or len(action) != 1:
            print('Invalid input')
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print(f"Car has driven {my_car.odometer}")

        elif action == 'S':
            print(f"Average speed is {my_car.speed()} km/h")

        my_car.step()
        my_car.say_state()
