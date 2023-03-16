from project.animals import animal
from project.animals import birds
from project.animals.birds import Owl
from project.food import Meat, Vegetable



owl = Owl("Pip", 10, 10)
#self.assertEqual(str(owl), "Owl [Pip, 10, 10, 0]")
meat = Meat(4)
print(owl.make_sound())
#self.assertEqual(owl.make_sound(), "Hoot Hoot")
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
#self.assertEqual(owl.feed(veg), "Owl does not eat Vegetable!")
#self.assertEqual(str(owl), "Owl [Pip, 10, 11.0, 4]")