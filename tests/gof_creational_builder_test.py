import unittest
from patterns.gof_creational_builder import PizzaBuilder, MargheritaPizzaBuilder, PizzaDirector

class TestPizzaBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = PizzaBuilder()
        self.director = PizzaDirector(self.builder)
        self.pizza = self.director.make_pizza("Whole Wheat", "BBQ", ["Chicken", "Onion", "Pepper"])

    def test_dough_type_base_builder(self):
        self.assertEqual(self.pizza._dough, "Whole Wheat", "Dough type should be 'Whole Wheat'")

    def test_sauce_type_base_builder(self):
        self.assertEqual(self.pizza._sauce, "BBQ", "Sauce should be 'BBQ'")

    def test_toppings_base_builder(self):
        expected_toppings = ["Chicken", "Onion", "Pepper"]
        for topping in expected_toppings:
            self.assertIn(topping, self.pizza._toppings, f"Pizza should contain '{topping}'")

    def test_number_of_toppings_base_builder(self):
        self.assertEqual(len(self.pizza._toppings), 3, "Pizza should have exactly 3 toppings")

class TestMargheritaPizzaBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = MargheritaPizzaBuilder()
        self.director = PizzaDirector(self.builder)
        self.pizza = self.director.make_pizza()

    def test_dough_type_margherita_builder(self):
        self.assertEqual(self.pizza._dough, "Thin Crust", "Dough type should be 'Thin Crust'")

    def test_sauce_type_margherita_builder(self):
        self.assertEqual(self.pizza._sauce, "Tomato", "Sauce should be 'Tomato'")

    def test_toppings_margherita_builder(self):
        expected_toppings = ["Mozzarella", "Basil"]
        for topping in expected_toppings:
            self.assertIn(topping, self.pizza._toppings, f"Pizza should contain '{topping}'")

    def test_number_of_toppings_margherita_builder(self):
        self.assertEqual(len(self.pizza._toppings), 2, "Margherita Pizza should have exactly 2 toppings")

if __name__ == '__main__':
    unittest.main()