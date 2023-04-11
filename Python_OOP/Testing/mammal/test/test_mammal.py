import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.animal = Mammal('Gosho', 'Monkey', 'AAaaa')

    def test_init(self):
        self.assertEqual(self.animal.name, 'Gosho')
        self.assertEqual(self.animal.type, 'Monkey')
        self.assertEqual(self.animal.sound, 'AAaaa')

    def test_make_sound(self):
        self.assertEqual(self.animal.make_sound(), "Gosho makes AAaaa")

    def test_get_kingdom(self):
        self.assertEqual(self.animal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.animal.info(), "Gosho is of type Monkey")


if __name__ == '__main__':
    unittest.main()