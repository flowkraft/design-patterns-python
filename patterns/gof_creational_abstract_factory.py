from abc import ABC, abstractmethod

# AbstractFactory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

# ConcreteFactory1
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_window(self):
        return WindowsWindow()

# ConcreteFactory2
class MotifFactory(GUIFactory):
    def create_button(self):
        return MotifButton()

    def create_window(self):
        return MotifWindow()

# AbstractProductA
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

# AbstractProductB
class Window(ABC):
    @abstractmethod
    def paint(self):
        pass

# ProductA1
class WindowsButton(Button):
    def paint(self):
        print("Rendering button in Windows style")

# ProductB1
class WindowsWindow(Window):
    def paint(self):
        print("Rendering window in Windows style")

# ProductA2
class MotifButton(Button):
    def paint(self):
        print("Rendering button in Motif style")

# ProductB2
class MotifWindow(Window):
    def paint(self):
        print("Rendering window in Motif style")

# Client
class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.window = factory.create_window()

    def paint(self):
        self.button.paint()
        self.window.paint()

# Example usage
if __name__ == "__main__":
    factory = WindowsFactory()
    app = Application(factory)
    app.paint()
