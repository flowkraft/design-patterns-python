import unittest
from patterns.gof_creational_abstract_factory import WindowsFactory, MotifFactory, WindowsButton, WindowsWindow, MotifButton, MotifWindow

class TestAbstractFactory(unittest.TestCase):
    def test_windows_factory(self):
        factory = WindowsFactory()
        button = factory.create_button()
        window = factory.create_window()
        self.assertIsInstance(button, WindowsButton)
        self.assertIsInstance(window, WindowsWindow)

    def test_motif_factory(self):
        factory = MotifFactory()
        button = factory.create_button()
        window = factory.create_window()
        self.assertIsInstance(button, MotifButton)
        self.assertIsInstance(window, MotifWindow)

if __name__ == '__main__':
    unittest.main()