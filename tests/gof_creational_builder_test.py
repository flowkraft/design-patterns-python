import unittest
from pizza_builder import PizzaBaseBuilder, MargheritaPizzaBuilder, PizzaDirector

class TestPizzaBaseBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = PizzaBaseBuilder()
        self.director = PizzaDirector(self.builder)
        self.pizza = self.director.make_pizza().prepare_dough("Whole Wheat").add_sauce("BBQ").add_toppings(["Chicken", "Onion", "Pepper"]).build()

    def test_dough_type_base_builder(self):
        self.assertEqual(self.pizza.dough, "Whole Wheat", "Dough type should be 'Whole Wheat'")

    def test_sauce_type_base_builder(self):
        self.assertEqual(self.pizza.sauce, "BBQ", "Sauce should be 'BBQ'")

    def test_toppings_base_builder(self):
        expected_toppings = ["Chicken", "Onion", "Pepper"]
        for topping in expected_toppings:
            self.assertIn(topping, self.pizza.toppings, f"Pizza should contain '{topping}'")

    def test_number_of_toppings_base_builder(self):
        self.assertEqual(len(self.pizza.toppings), 3, "Pizza should have exactly 3 toppings")

class TestMargheritaPizzaBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = MargheritaPizzaBuilder()
        self.director = PizzaDirector(self.builder)
        self.pizza = self.director.make_pizza()

    def test_dough_type_margherita_builder(self):
        self.assertEqual(self.pizza.dough, "Thin Crust", "Dough type should be 'Thin Crust'")

    def test_sauce_type_margherita_builder(self):
        self.assertEqual(self.pizza.sauce, "Tomato", "Sauce should be 'Tomato'")

    def test_toppings_margherita_builder(self):
        expected_toppings = ["Mozzarella", "Basil"]
        for topping in expected_toppings:
            self.assertIn(topping, self.pizza.toppings, f"Pizza should contain '{topping}'")

    def test_number_of_toppings_margherita_builder(self):
        self.assertEqual(len(self.pizza.toppings), 2, "Margherita Pizza should have exactly 2 toppings")

if __name__ == '__main__':
    unittest.main()
