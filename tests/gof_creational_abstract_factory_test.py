import pytest
from gof_creational_abstract_factory import WindowsFactory, MotifFactory, WindowsButton, WindowsWindow, MotifButton, MotifWindow

def test_windows_factory():
    factory = WindowsFactory()
    button = factory.create_button()
    window = factory.create_window()
    assert isinstance(button, WindowsButton)
    assert isinstance(window, WindowsWindow)

def test_motif_factory():
    factory = MotifFactory()
    button = factory.create_button()
    window = factory.create_window()
    assert isinstance(button, MotifButton)
    assert isinstance(window, MotifWindow)
