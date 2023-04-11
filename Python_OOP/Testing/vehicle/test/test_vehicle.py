import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.BMW = Vehicle(30, 200)

    def test_init(self):
        self.assertEqual(self.BMW.fuel_consumption, self.BMW.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(1.25, self.BMW.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(self.BMW.fuel, self.BMW.capacity)
        self.assertEqual(self.BMW.fuel, 30)
        self.assertEqual(self.BMW.horse_power, 200)

    def test_drive(self):
        self.BMW.drive(4)
        self.assertEqual(self.BMW.fuel, 25)
        with self.assertRaises(Exception) as ex:
            self.BMW.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.BMW.drive(4)
        self.BMW.refuel(4)
        self.assertEqual(self.BMW.fuel, 29)
        with self.assertRaises(Exception) as ex:
            self.BMW.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        self.assertEqual(str(self.BMW), f"The vehicle has 200 horse power with 30 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()