import unittest
from Car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car()


class TestInit(TestCar):
    def test_initial_speed(self):
        self.assertEqual(self.car.speed, 0)

    def test_initial_odometer(self):
        self.assertEqual(self.car.odometer, 0)

    def test_initial_time(self):
        self.assertEqual(self.car.time, 0)

    def test_initial_fuel_tank(self):
        self.assertEqual(self.car.fuel_tank_capacity, 40)

    def test_initial_fuel(self):
        self.assertEqual(self.car.fuel, 20)


class TestAccelerate(TestCar):

    def test_accelerate_from_zero(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_multiple_from_zero(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)


class TestBreak(TestCar):

    def test_brake(self):
        self.car.accelerate()
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_multiple_brakes(self):
        for _ in range(5):
            self.car.accelerate()
        for _ in range(3):
            self.car.brake()
        self.assertEqual(self.car.speed, 10)

    def test_should_not_allow_negative_speed(self):
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_multiple_brakes_at_zero(self):
        for _ in range(3):
            self.car.brake()
        self.assertEqual(self.car.speed, 0)


class TestRefuel(TestCar):

    def test_refuel(self):
        self.car.refueling()
        self.assertEqual(self.car.fuel, self.car.fuel_tank_capacity)
