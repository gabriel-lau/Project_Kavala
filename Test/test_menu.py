import pytest
from SRC.Main import *

# Test for displaying menu
def test_displayMenu():
    menu = displayMenu()
    assert menu == ("MAIN MENU\n" 
                    "=========\n"
                    "[1] Read and load maze from file\n"
                    "[2] View maze\n"
                    "[3] Play maze game\n"
                    "[4] Configure current maze\n\n"
                    "[0] Exit Maze\n")
