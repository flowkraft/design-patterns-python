import pytest
from your_module import WindowsFactory, MotifFactory, WindowsButton, WindowsWindow, MotifButton, MotifWindow

def test_windows_factory():
    factory = WindowsFactory()
    button = factory
