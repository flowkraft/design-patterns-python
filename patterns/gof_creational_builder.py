# Entity: Product
class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, toppings: {', '.join(self.toppings) if self.toppings else 'no toppings'}"

# Entity: Builder Interface
class PizzaBuilder:
    def prepare_dough(self, dough):
        pass

    def add_sauce(self, sauce):
        pass

    def add_toppings(self, toppings):
        pass

    def build(self):
        pass

# Entity: ConcreteBuilder
class PizzaBaseBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def prepare_dough(self, dough):
        self.pizza.set_dough(dough)
        return self

    def add_sauce(self, sauce):
        self.pizza.set_sauce(sauce)
        return self

    def add_toppings(self, toppings):
        for topping in toppings:
            self.pizza.add_topping(topping)
        return self

    def build(self):
        return self.pizza

# Entity: ConcreteBuilder
class MargheritaPizzaBuilder(PizzaBaseBuilder):
    def __init__(self):
        super().__init__()

    def prepare_dough(self):
        super().prepare_dough("Thin Crust")
        return self

    def add_sauce(self):
        super().add_sauce("Tomato")
        return self

    def add_toppings(self):
        super().add_toppings(["Mozzarella", "Basil"])
        return self

# Entity: Director
class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder

    def make_pizza(self, dough=None, sauce=None, toppings=None):
        if dough:
            self._builder.prepare_dough(dough)
        if sauce:
            self._builder.add_sauce(sauce)
        if toppings:
            self._builder.add_toppings(toppings)
        return self._builder.build()

# Client code example
if __name__ == "__main__":
    # Using the base builder for a custom pizza
    customPizzaBuilder = PizzaBaseBuilder()
    director = PizzaDirector(customPizzaBuilder)
    customPizza = director.make_pizza().prepare_dough("Whole Wheat").add_sauce("BBQ").add_toppings(["Chicken", "Onion", "Pepper"]).build()
    print("Custom Pizza:", customPizza)

    # Using the MargheritaPizzaBuilder
    margheritaBuilder = MargheritaPizzaBuilder()
    director = PizzaDirector(margheritaBuilder)
    margheritaPizza = director.make_pizza()
    print("Margherita Pizza:", margheritaPizza)
