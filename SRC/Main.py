import csv
maze_list = []

# Display menu
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


# [1] Read and load file
def read_file(maze_list):
    print ("Option [1]: Read and load maze from file")
    print ("==========================================")
    filename = input("Enter the name of the data file: ")

    if '.csv' in filename:
        with open (filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                maze_list.append(row)

        if len(maze_list) != 0:
            store_start_end(maze_list)
            print("Number of lines read: ", len(maze_list), "\n")
        else:
            print("No maze found in file!")

    else:
        print("Invalid file type!")
    
    return maze_list


def store_start_end(maze_list):
    for list in maze_list:
        for index, list in enumerate(maze_list):
            if 'A' in list:
                row_A = index + 1
                column_A = maze_list[index].index('A') + 1
            if 'B' in list:
                row_B = index + 1
                column_B = maze_list[index].index('B') + 1
    try:
        row_A and row_B
    except NameError:
        print("Maze does not have a start or end point.")
    else:
        row_column_list = [[row_A, column_A], [row_B, column_B]]
        return row_column_list


# [2] Display maze
def display_maze(maze_list):
    if maze_list == []:
        print("No maze in memory. Load your maze file through Option 1!")
    else:    
        print ("Option [2]: View maze")
        print ("==========================================")
        print('\n'.join([str(lst) for lst in maze_list]))

    return maze_list


# [3] Play maze game
def play_game():
    return True


# [4] Configure maze
def configure_maze(maze_list):
    #To Display configuring maze menu
    displayconfigure_maze_menu(maze_list)
    option = input("Enter your option: ")
    print("\n")
    if(option == "0"):
        exitConfigure()
    else:
        coorOpt = input(displayConfigureInput(maze_list))
        if(option == "1"):
            ChangeCoordToX(maze_list, coorOpt)
        elif(coorOpt == "B"):
            returnConfigure(maze_list)
        elif(coorOpt == "M"):
            returnMain(maze_list)
    return True

# [4] 1 Display Configure maze menu
def displayconfigure_maze_menu(maze_list):
    #When user has not loaded the maze list
    if(maze_list == []):
        print("No maze in memory. Load your maze file through Option 1!\n")
        #Have to comment this out when running pytest
        #main(maze_list)
        return False
    else:
        #Display configure maze menu
        Statement =(
        "\nCONFIGURATION MENU\n"
        "==================\n"
        "[1] Create wall\n"
        "[2] Create passageway\n"
        "[3] Create start point\n"
        "[4] Create end point\n\n"

        "[0] Exit to Main Menu\n")
        print(Statement)
        return True
    
# [4] 2 Display input for when to create item in maze
def displayConfigureInput(maze_list):
    #To display the maze list first
    print('\n'.join([str(lst) for lst in maze_list]))
    print('\n')
    Statement = ("Enter the coordinate of the item you wish to change E.g. Row, Column\n"
    "'B' to return to Configure Menu.\n"
    "'M' to return to Main Menu: ")
    return Statement

# [4] 3 Exit Config menu
def exitConfigure():
    #To exit from config menu
    statement = "\nExited from Configuration Menu"
    print(statement)
    #main(maze_list)
    return statement

# [4] 4 Return to Config menu
def returnConfigure(maze_list):
    statement = "\nReturning to configuration menu"
    print(statement)
    configure_maze(maze_list)
    return statement

# [4] 5 Return to Main menu
def returnMain(maze_list):
    statement = "\nReturning to Main menu"
    print(statement)
    #main(maze_list)
    return statement

# [4] 6 Change Coordinate to X
def ChangeCoordToX(maze_list, coor):
    firstCoor = int(coor[0]) - 1
    secondCoor = int(coor[-1]) - 1
    print("Changed " + maze_list[firstCoor][secondCoor] + "-> X")
    maze_list[firstCoor][secondCoor] = "X"
    print('\n'.join([str(lst) for lst in maze_list]))
    print('\n')
    statement = "\nChanged coordinate to X"
    return statement


# MAIN FUNCTION 
def main(maze_list):
    while True:
        option = display_menu()
        option = input("Enter your option: ")
        print()

        if option.isdigit():
            option = int(option)

            if option == 1:
                maze_list = []
                read_file(maze_list)
            elif option == 2:
                maze_list = display_maze(maze_list)
            elif option == 3:
                play_game()
            elif option == 4:
                configure_maze(maze_list)  
            elif option == 0:
                print ("Thanks for playing Maze!")
                return False
            else:
                print ("Invalid option. Please try again!")
        else:
            print ("Invalid option. Please try again!")
            
        print()
# TODO: For some reason there is an error when you try to run the main() function!!!
#main(maze_list)
