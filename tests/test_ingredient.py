import unittest
from praktikum.ingredient import Ingredient
from parameterized import parameterized


class TestIngredient(unittest.TestCase):

    @parameterized.expand([
        ("test_ingredient1", "type1", 50),
        ("test_ingredient2", "type2", 60),
        ("test_ingredient3", "type3", 70),
    ])
    def test_get_name(self, name, ingredient_type, price):
        ingredient = Ingredient(name, ingredient_type, price)
        assert ingredient.get_name(), name

    @parameterized.expand([
        ("test_ingredient1", "type1", 50),
        ("test_ingredient2", "type2", 60),
        ("test_ingredient3", "type3", 70),
    ])
    def test_get_price(self, name, ingredient_type, price):
        ingredient = Ingredient(name, ingredient_type, price)
        assert ingredient.get_price(), price
