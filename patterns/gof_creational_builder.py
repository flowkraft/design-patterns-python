# Entity: Product
class Pizza:
    def __init__(self):
        self._dough = ""
        self._sauce = ""
        self._toppings = []

    def set_dough(self, dough):
        self._dough = dough

    def set_sauce(self, sauce):
        self._sauce = sauce

    def add_topping(self, topping):
        self._toppings.append(topping)

    def __str__(self):
        return f"Pizza with {self._dough} dough, {self._sauce} sauce, toppings: {', '.join(self._toppings) if self._toppings else 'no toppings'}"

# Entity: Builder Interface
class PizzaBuilder:
    def __init__(self):
        self.default_dough = None
        self.default_sauce = None
        self.default_toppings = None
        self.pizza = Pizza()

    def prepare_dough(self, dough=None):
        if dough is None:
            dough = self.default_dough
        self.pizza.set_dough(dough)
        return self

    def add_sauce(self, sauce=None):
        if sauce is None:
            sauce = self.default_sauce
        self.pizza.set_sauce(sauce)
        return self

    def add_toppings(self, toppings=None):
        if toppings is None:
            toppings = self.default_toppings
        for topping in toppings:
            self.pizza.add_topping(topping)
        return self

    def build(self):
        pizza = self.pizza
        self.pizza = Pizza()  # Reset for next build
        return pizza

# Entity: ConcreteBuilder
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()
        self.default_dough = "Thin Crust"
        self.default_sauce = "Tomato"
        self.default_toppings = ["Mozzarella", "Basil"]

# Entity: Director
class PizzaDirector:
    def __init__(self, builder):
        assert isinstance(builder, PizzaBuilder), 'Builder must be an instance of PizzaBuilder'
        self._builder = builder

    def make_pizza(self, dough=None, sauce=None, toppings=None):
        self._builder.prepare_dough(dough)
        self._builder.add_sauce(sauce)
        self._builder.add_toppings(toppings)
        return self._builder.build()

# Client code example
if __name__ == "__main__":
    # Using the base builder for a custom pizza
    customPizzaBuilder = PizzaBuilder()
    director = PizzaDirector(customPizzaBuilder)
    customPizza = director.make_pizza(dough = "Whole Wheat", sauce= "BBQ", toppings = ["Chicken", "Onion", "Pepper"])
    print("Custom Pizza:", customPizza)

    # Using the MargheritaPizzaBuilder
    margheritaBuilder = MargheritaPizzaBuilder()
    director = PizzaDirector(margheritaBuilder)
    margheritaPizza = director.make_pizza()
    print("Margherita Pizza:", margheritaPizza)