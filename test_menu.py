import pytest
from src.main import *

# Test for displaying menu
def test_displayMenu():
    menu = display_menu()
    assert menu == ("MAIN MENU\n" 
                    "=========\n"
                    "[1] Read and load maze from file\n"
                    "[2] View maze\n"
                    "[3] Play maze game\n"
                    "[4] Configure current maze\n\n"
                    "[0] Exit Maze\n")

# TODO: Make unit tests for readFile(), displayMaze() , playGame() & configureMaze() once these functions are done
@pytest.mark.parametrize("option",[(1), (2), (3), (4), (5), (0), (-2), (-10), ('letters'), ('$$^@!')])
def test_SelectOption(option):
    # if option == 1:
    #     assert menu_function(1) == <return function for 1>
    # elif option == 2:
    #     assert menu_function(2) == <return function for 2>
    # elif option == 3:
    #     assert menu_function(3) == <return function for 3>
    # elif option == 4:
    #     assert menu_function(4) == <return function for 4>
    if option == 0:
        assert menu_function(0) == "Thanks for playing Maze!"
    else:
        assert menu_function(option) == "Invalid option. Please try again!"