import unittest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger(unittest.TestCase):

    def setUp(self):
        self.burger = Burger()
        self.bun_mock = Mock()
        self.ingredient_mock = Mock()

    def test_set_buns(self):
        self.burger.set_buns(self.bun_mock)
        assert self.burger.bun == self.bun_mock

    def test_add_ingredient(self):
        self.burger.add_ingredient(self.ingredient_mock)
        assert self.ingredient_mock in self.burger.ingredients

    def test_remove_ingredient(self):
        self.burger.ingredients.append(self.ingredient_mock)
        self.burger.remove_ingredient(0)
        assert self.ingredient_mock not in self.burger.ingredients

