import pytest
from SRC.Main import *
import mock

# ==================================================================
# Test for displaying menu
def test_display_menu():
    menu = display_menu()
    assert menu == ("MAIN MENU\n" 
                    "=========\n"
                    "[1] Read and load maze from file\n"
                    "[2] View maze\n"
                    "[3] Play maze game\n"
                    "[4] Configure current maze\n\n"
                    "[0] Exit Maze\n")

# ==================================================================
# TEST FOR GENERAL OPTIONS
# Test for invalid options
def test_select_invalid_option_5():
    with mock.patch('builtins.input', return_value=5):
        assert menu_function() == "Invalid option. Please try again!"

def test_select_invalid_option_letters():
    with mock.patch('builtins.input', return_value='letters'):
        assert menu_function() == "Invalid option. Please try again!"

def test_select_invalid_option_letters():
    with mock.patch('builtins.input', return_value="$$@#%"):
        assert menu_function() == "Invalid option. Please try again!"

# Test for error message
def test_select_option_0():
    with mock.patch('builtins.input', return_value=0):
        assert menu_function() == "Thanks for playing Maze!"

# ==================================================================
### Tests for reading file
@pytest.mark.parametrize("filename", [("maze.csv")])
def test_select_option_1(filename):
    with mock.patch('builtins.input', return_value=filename):
        assert menu_function() != ""

@pytest.mark.parametrize("filename", [("maze.csv")])
def test_read_maze(filename):
    maze_list = read_file(filename)
    assert maze_list != []
    
@pytest.mark.parametrize("filename", [("maze")])
def test_cannot_read_maze(filename):
    error = read_file(filename)
    assert error == "Invalid file type!"

@pytest.mark.parametrize("filename", [("maze-empty.csv")])
def test_no_maze_found(filename):
    error = read_file(filename)
    assert error == "No maze found in file!"

@pytest.mark.parametrize("filename", [("maze.csv")])
def test_store_maze_have_start_end(filename):
    maze_list = read_file(filename)
    assert store_start_end(maze_list) != []

@pytest.mark.parametrize("filename", [("maze-no-start-end.csv")])
def test_store_maze_no_start_end(filename):
    maze_list = read_file(filename)
    assert store_start_end(maze_list) == "Maze does not have a start or end point."

# ==================================================================
# Tests for view maze
def test_select_option_2():
    with mock.patch('builtins.input', return_value=2):
        assert menu_function() != []