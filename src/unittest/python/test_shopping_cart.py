import unittest
from shopping_cart import ShoppingCart
class TestShoppingCart(unittest.TestCase):

    def test_empty_cart_has_zero_total(self):
        cart = ShoppingCart()
        self.assertEqual(cart.total(), 0)

    def test_adding_item_updates_total(self):
        cart = ShoppingCart()
        cart.add_item(500)
        self.assertEqual(cart.total(), 500)

    def test_adding_multiple_item_updates_total(self):
        cart = ShoppingCart()
        cart.add_item(500)
        cart.add_item(400)
        self.assertEqual(cart.total(), 900)

    def test_10_percent_order_gt_1000(self):
        cart = ShoppingCart()
        cart.add_item(500)
        cart.add_item(600)
        self.assertEqual(cart.total(), 990)
