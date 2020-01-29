# Display main menu
def display_menu():
    menu = ("MAIN MENU\n" 
            "=========\n"
            "[1] Read and load maze from file\n"
            "[2] View maze\n"
            "[3] Play maze game\n"
            "[4] Configure current maze\n\n"
            "[0] Exit Maze\n")

    print(menu)
    return menu

# Allow user to choose option
def choose_option():
    menu_option = int(input("Enter your option: "))
    return menu_option

# TODO: Uncomment functions when you unit test them. In test_menu, include expected return values
def menu_function(menu_option):
    if menu_option == 1:
        # return readFile()
        return "Invalid option. Please try again!"
    elif menu_option == 2:
        # return displayMaze()
        return "Invalid option. Please try again!"
    elif menu_option == 3:
        # return playGame()
        return "Invalid option. Please try again!"
    elif menu_option == 4:
        # return configureMaze()
        return "Invalid option. Please try again!"
    elif menu_option == 0:
        return "Thanks for playing Maze!"
    else:
        return "Invalid option. Please try again!"

# # Reads maze file in .csv format
# def readFile():
#     return True

# # Displays the maze
# def displayMaze():
#     return True

# # Play maze game
# def playGame():
#     return True

# # Configure maze
# def configureMaze():
#     return True

# Global -------------------------------------
# while True:
#     displayMenu()
#     if chooseOption() == 0:
#          break
#     print()