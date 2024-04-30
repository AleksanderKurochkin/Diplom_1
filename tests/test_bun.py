import unittest
from praktikum.bun import Bun
from parameterized import parameterized


class TestBun(unittest.TestCase):

    @parameterized.expand([
        ("test_bun1", 100),
        ("test_bun2", 200),
        ("test_bun3", 150),
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @parameterized.expand([
        ("test_bun1", 100),
        ("test_bun2", 200),
        ("test_bun3", 150),
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
