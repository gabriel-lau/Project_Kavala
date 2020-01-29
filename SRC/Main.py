import csv

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


def menu_function():
    menu_option = input("Enter your option: ")
    if menu_option == 1:
        print()
        print ("Option [1] Read and load maze from file")
        print ("=======================================")
        filename = input("Enter the name of the data file: ")
        read_file(filename)
        return filename
    elif menu_option == 2:
        print ("Option [2]: View maze")
        print ("=======================================")
        try:
            mazeList
        except NameError:
            error = "No maze in memory. Load your maze file through Option 1 now!"
            return error
        else:
            displayMaze(mazeList)
            return mazeList
    elif menu_option == 3:
        playGame()
        # return
    elif menu_option == 4:
        configureMaze()
        # return 
    elif menu_option == 0:
        print ("Thanks for playing Maze!")
        return "Thanks for playing Maze!"
    else:
        print ("Invalid option. Please try again!")
        return "Invalid option. Please try again!"


# Reads maze file in .csv format
def read_file(filename):
    mazeList = []
    if '.csv' in filename:
        with open (filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                mazeList.append(row)

        if len(mazeList) != 0:
            store_start_end(mazeList)
            print("Number of lines read: ", len(mazeList))
            return mazeList
        else:
            error = "No maze found in file!"
            print (error)
    else:
        error = "Invalid file type!"
        print(error)
    return error


# Store row and columns of start and end
def store_start_end(mazeList):
    for list in mazeList:
        for index, list in enumerate(mazeList):
            if 'A' in list:
                row_A = index + 1
                column_A = mazeList[index].index('A') + 1
            if 'B' in list:
                row_B = index + 1
                column_B = mazeList[index].index('B') + 1

        try:
            row_A and row_B
        except NameError:
            error = "Maze does not have a start or end point."
            return error
        else:
            row_column_list = [[row_A, column_A], [row_B, column_B]]
            return row_column_list


# Displays the maze
def displayMaze(mazeList):
    print('\n'.join([str(lst) for lst in mazeList]))
    return mazeList

# # Play maze game
# def playGame():
#     return True

# # Configure maze
# def configureMaze():
#     return True

# Global -------------------------------------
# flag = menu_function()
# while flag != "Thanks for playing Maze!":
#     display_menu()
#     menu_function()
#     print()