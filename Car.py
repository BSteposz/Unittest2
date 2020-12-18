
class Car(object):
    """ Random class car"""
    def __init__(self, speed=0):
        """ Initialize default speed, distance and time """
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def sey_state(self):
        """ Print current speed in km/k"""
        print(f"I'm going {self.speed} km/h")
