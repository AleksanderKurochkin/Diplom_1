import unittest
from unittest.mock import Mock, patch
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database


class TestDatabase(unittest.TestCase):

    @patch('praktikum.database.Database.available_buns')
    def test_available_buns(self, mock_available_buns):
        mock_available_buns.return_value = [Mock(spec=Bun)]
        database = Database()
        buns = database.available_buns()
        assert len(buns) > 0

    @patch('praktikum.database.Database.available_ingredients')
    def test_available_ingredients(self, mock_available_ingredients):
        mock_available_ingredients.return_value = [Mock(spec=Ingredient)]
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) > 0
