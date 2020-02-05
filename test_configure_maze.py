import pytest
from SRC.Main import *
import mock
import io

maze_normal = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
no_maze = []
coor = "2, 3" #Coordinates to an O
opt = "4"
optFail = "5"
#Coordinates to an A
firstA = 1
secondA = 6
#Coordinates to a B
firstB = 7
secondB = 1

itemCheck = "X"
itemChange = "A"
#Coordinates to a X
firstX = 0
secondX = 3

#Check if there is maze, thus display config menu
def test_ConfigurationOptionMethod():
    assert displayconfigure_maze_menu(maze_normal) == True

#Check if there is no maze (Failing test case)
def test_ConfigurationOptionMethodFailed():
    assert displayconfigure_maze_menu(no_maze) == False

#Check once user input to change to a selected maze item, this statement displays
def test_ConfigurationOptionsSelected():
    Statement = ("Enter the coordinate of the item you wish to change E.g. Row, Column\n"
    "'B' to return to Configure Menu.\n"
    "'M' to return to Main Menu: ")
    assert displayConfigureInput(maze_normal) == Statement

#Check if program exits to main menu when 0 is inputted
def test_ConfigurationExit():
    statement = "\nExited from Configuration Menu"
    assert exitConfigure() == statement

#Check if program returns to config menu when B is inputted
def test_ConfigurationReturn():
    statement = "\nReturning to configuration menu"
    assert returnConfigure(maze_normal) == statement

#Check if program returns to main menu when M is inputted
def test_MainReturn():
    statement = "\nReturning to Main menu"
    assert returnMain(maze_normal) == statement

#Check if item of coordinate 'coor' changes to X
def test_ChangeCoordinatetoX():
    statement = "\nChanged coordinate to X"
    assert ChangeCoordToX(maze_normal, coor) == statement

#When the selected coordinate is A for changing to X
def test_ChecksForChangeXCaseA():
    statement = "\nThe selected coordinate start point has been changed"
    #firstA and secondA are the coordinates to "A" in maze_normal
    assert CheckForChangeO(maze_normal, firstA, secondA) == statement

#When the selected coordinate is B for changing to X
def test_ChecksForChangeXCaseB():
    statement = "\nThe selected coordinate end point has been changed"
    assert CheckForChangeO(maze_normal, firstB, secondB) == statement

#Check if item of coordinate 'coor' changes to O
def test_ChangeCoordinatetoO():
    statement = "\nChanged coordinate to O"
    assert ChangeCoordToO(maze_normal, coor) == statement

#When the selected coordinate is A for changing to O
def test_ChecksForChangeOCaseA():
    statement = "\nThe selected coordinate start point has been changed"
    #firstA and secondA are the coordinates to "A" in maze_normal
    assert CheckForChangeO(maze_normal, firstA, secondA) == statement

#When the selected coordinate is B for changing to O
def test_ChecksForChangeOCaseB():
    statement = "\nThe selected coordinate end point has been changed"
    assert CheckForChangeO(maze_normal, firstB, secondB) == statement

#Check if item of coordinate 'coor' changes to A
def test_ChangeCoordinatetoA():
    statement = "\nChanged coordinate to A"
    assert ChangeCoordToA(maze_normal, coor) == statement

#Checks if selected item (B) to change to A
def test_ChecksForChangeA():
    statement = "\n Your end point and start point exchanged places!"
    assert CheckForChangeA(maze_normal, firstB, secondB) == statement

#Checks if selected item (A) to change to A
def test_ChecksForChangeA():
    statement = "\n That is already your start point"
    assert CheckForChangeA(maze_normal, firstA, secondA) == statement

#Check if item of coordinate 'coor' changes to B
def test_ChangeCoordinatetoB():
    statement = "\nChanged coordinate to B"
    assert ChangeCoordToB(maze_normal, coor) == statement

#Checks if selected item (A) to change to B
def test_ChecksForChangeB():
    statement = "\n Your end point and start point exchanged places!"
    assert CheckForChangeA(maze_normal, firstA, secondA) == statement

#Checks if selected item (B) to change to B
def test_ChecksForChangeB():
    statement = "\n That is already your end point"
    assert CheckForChangeA(maze_normal, firstB, secondB) == statement



#Check if option inputted is not less than equal to 0 and more than 4
def test_CheckOpt():
    assert CheckOption(opt) == True
    
#Check if option inputted is less than equal to 0 or more than 4 (Failling test case)
def test_CheckOptFail():
    assert CheckOption(optFail) == False

#Check around a maze item function
#itemCheck = item to find around the coordinated item
def test_CheckAroundMazeItem():
    assert CheckAroundItem(firstA, secondA, itemCheck, itemChange, maze_normal) == True
