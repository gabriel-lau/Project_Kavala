import pytest
from SRC.Main import *
import mock
import io

maze_normal = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
no_maze = []
coor = "2, 3"

def test_ConfigurationOptionMethod():
    assert displayconfigure_maze_menu(maze_normal) == True

def test_ConfigurationOptionMethodFailed():
    assert displayconfigure_maze_menu(no_maze) == False

def test_ConfigurationOptionsSelected():
    Statement = ("Enter the coordinate of the item you wish to change E.g. Row, Column\n"
    "'B' to return to Configure Menu.\n"
    "'M' to return to Main Menu: ")
    assert displayConfigureInput(maze_normal) == Statement

def test_ConfigurationExit():
    statement = "\nExited from Configuration Menu"
    assert exitConfigure() == statement

def test_ConfigurationReturn():
    statement = "\nReturning to configuration menu"
    assert returnConfigure(maze_normal) == statement

def test_MainReturn():
    statement = "\nReturning to Main menu"
    assert returnMain(maze_normal) == statement

def test_ChangeCoordinatetoX():
    statement = "\nChanged coordinate to X"
    assert ChangeCoordToX(maze_normal, coor) == statement

def test_ChangeCoordinatetoO():
    statement = "\nChanged coordinate to O"
    assert ChangeCoordToO(maze_normal, coor) == statement

def test_ChangeCoordinatetoA():
    statement = "\nChanged coordinate to A"
    assert ChangeCoordToA(maze_normal, coor) == statement

def test_ChangeCoordinatetoB():
    statement = "\nChanged coordinate to B"
    assert ChangeCoordToB(maze_normal, coor) == statement
