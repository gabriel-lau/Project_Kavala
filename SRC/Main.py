import csv
import os.path
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


#############################################################################################################################


# [1] Read and load file
def read_file(maze_list):
    print ("Option [1]: Read and load maze from file")
    print ("==========================================")
    filename = input("Enter the name of the data file: ")

    # Validation checking for filename
    if '.csv' in filename:
        if os.path.exists(filename):
            with open (filename) as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    maze_list.append(row)

            if len(maze_list) != 0:
                store_start_end(maze_list)
                print("Number of lines read: ", len(maze_list), "\n")
            else:
                print("No maze found in file!\n")
        else:
            print("CSV file not found!\n")
    else:
        print("Invalid file type! Only CSV files accepted.\n")
    
    return maze_list


# Store the coordinates (row, column) of the start and end points of the maze
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


#############################################################################################################################


# [2] Display maze
def display_maze(maze_list):
    if maze_list == []:
        print("No maze in memory. Load your maze file through Option 1!")
    else:    
        print ("Option [2]: View maze")
        print ("==========================================")
        print('\n'.join([str(lst) for lst in maze_list]))

    return maze_list


#############################################################################################################################


# [3] Play maze game
# ../maze.csv
def play_game(maze_list): #Load Maze
    for list in maze_list:
        for index, list in enumerate(maze_list):
            if 'A' in list:
                row_A = index 
                column_A = maze_list[index].index('A') 
            if 'B' in list:
                row_B = index 
                column_B = maze_list[index].index('B') 
                

    if maze_list == []:
        print("No maze in memory. Load your maze file through Option 1!")
    else:    
        print ("Option [3]: Play maze game")
        print ("==========================================")
        print('\n'.join([str(lst) for lst in maze_list]))
        print('\n''Location of Start (A) = ' + '(Row ' + str(row_A) + ', Column ' + str(column_A) +')') # Printing out location
        print('\n''Location of Start (B) = ' + '(Row ' + str(row_B) + ', Column ' + str(column_B) +')')
    movement = input(str('\n'"Press 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MAIN MENU: ")) # Movement code
    start_coords = (row_A,column_A)

    if movement == 'M':
        return main(maze_list)
    elif movement == 'W':
        if maze_list[start_coords[0]-1][start_coords[1]] == 'B': # Check if it is the end
            print("Congrats!")
            quit()
        if maze_list[start_coords[0]-1][start_coords[1]] == 'O' or maze_list[start_coords[0]-1][start_coords[1]] == 'B':# Check if it is valid move
            maze_list[start_coords[0]][start_coords[1]] = 'O'
            maze_list[start_coords[0]-1][start_coords[1]] = 'A'
        else:
            print("Invalid move"+"\n")
        return play_game(maze_list)
    elif movement == 'A':
        if maze_list[start_coords[0]][start_coords[1]-1] == 'B':
            print("Congrats!")
            quit()
        if maze_list[start_coords[0]][start_coords[1]-1] == 'O' or maze_list[start_coords[0]][start_coords[1]-1] == 'B':
            maze_list[start_coords[0]][start_coords[1]] = 'O'
            maze_list[start_coords[0]][start_coords[1]-1] = 'A'
        else:
            print("Invalid move"+"\n")
        return play_game(maze_list)
    elif movement == 'S':
        if maze_list[start_coords[0]+1][start_coords[1]] == 'B':
            print("Congrats!")
            quit()
        if maze_list[start_coords[0]+1][start_coords[1]] == 'O' or maze_list[start_coords[0]+1][start_coords[1]] == 'B':
            maze_list[start_coords[0]][start_coords[1]] = 'O'
            maze_list[start_coords[0]+1][start_coords[1]] = 'A'
        else:
            print("Invalid move"+"\n")
        return play_game(maze_list)
    elif movement == 'D':
        if maze_list[start_coords[0]][start_coords[1]+1] == 'B':
            print("Congrats!")
            quit()
        if maze_list[start_coords[0]][start_coords[1]+1] == 'O' or maze_list[start_coords[0]][start_coords[1]+1] == 'B':
            maze_list[start_coords[0]][start_coords[1]] = 'O'
            maze_list[start_coords[0]][start_coords[1]+1] = 'A'
        else:
            print("Invalid move"+"\n")
        return play_game(maze_list)
    else:
        print("Invalid Character. Please try again!")
        return play_game(maze_list)

    #return maze_list


#############################################################################################################################


# [4] Configure maze
def configure_maze(maze_list):
    rlen = 0
    clen = 0
    #To check highest num of coordinates
    for row in maze_list:
        rlen += 1
    for col in maze_list[0]:
        clen += 1
            
    #To Display configuring maze menu
    displayconfigure_maze_menu(maze_list)
    #Enter option for config menu
    option = input("Enter your option: ")
    print("\n")
    #if users choose to exit to main menu
    if(option == "0"):
        exitConfigure()
    #if users do not exit to main menu
    else:
        #To check if user does not input more than "4" or less than equal to 0
        if(CheckOption(option)):
            coorOpt = input(displayConfigureInput(maze_list))
            if(len(coorOpt) > 1): #Means its a coordinate
                firstnum = 0
                secondnum = 0
                try:
                    firstnum = int(coorOpt[0])
                    secondnum = int(coorOpt[-1])
                except:
                    pass
                if((len(coorOpt) == 3) and (0 < int(firstnum) <= rlen and 0 < int(secondnum) <= clen)):
                    if(option == "1" and coorOpt.isalpha() != True):
                        ChangeCoordToX(maze_list, coorOpt)
                    elif(option == "2" and coorOpt.isalpha() != True):
                        ChangeCoordToO(maze_list, coorOpt)
                    elif(option == "3" and coorOpt.isalpha() != True):
                        ChangeCoordToA(maze_list, coorOpt)
                    elif(option == "4" and coorOpt.isalpha() != True):
                        ChangeCoordToB(maze_list, coorOpt)
                else:
                    print("Please provide correct inputs of coordinate make sure it is in this form: row,column\n")
            elif(coorOpt == "B" or coorOpt == "M"):
                if(option != "0" and coorOpt == "B"):
                    returnConfigure(maze_list)
                elif(option != "0" and coorOpt == "M"):
                    returnMain(maze_list)
            else:
                print("Please provide correct coordinates of the item you wish to change!\n"
                    "This might look like a game but its not!")
                
    return True

# [4] 1 Display Configure maze menu
def displayconfigure_maze_menu(maze_list):
    #When user has not loaded the maze list
    if(maze_list == []):
        print("No maze in memory. Load your maze file through Option 1!\n")
        #Have to comment this out when running pytest
        main(maze_list)
        return False
    else:
        #Display maze list first
        print("\n")
        print('\n'.join([str(lst) for lst in maze_list]))
        print('\n')
        #Display configure maze menu
        Statement =(
        "CONFIGURATION MENU\n"
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
    #Require user to enter coordinate or exit
    Statement = ("Enter the coordinate of the item you wish to change E.g. Row,Column\n"
    "'B' to return to Configure Menu.\n"
    "'M' to return to Main Menu: ")
    return Statement

# [4] 3 Exit Config menu
def exitConfigure():
    #To exit from config menu
    statement = "\nExited from Configuration Menu"
    print(statement)
    #To run the app again from Main menu
    #Required to comment this out since it has input
    main(maze_list)
    return statement
    

# [4] 4 Return to Config menu
def returnConfigure(maze_list):
    statement = "\nReturning to configuration menu"
    print(statement)
    #To run the app from Configuration menu
    #Required to comment this out since it has input
    configure_maze(maze_list)
    return statement
    

# [4] 5 Return to Main menu
def returnMain(maze_list):
    statement = "\nReturning to Main menu"
    print(statement)
    #To run the app again from Main menu
    #Required to comment this out since it has input
    main(maze_list)
    return statement

# [4] 6 Change Coordinate to X
def ChangeCoordToX(maze_list, coor):
    firstCoor = int(coor[0]) - 1
    secondCoor = int(coor[-1]) - 1
    print(CheckForChangeX(maze_list, firstCoor, secondCoor))
    print("Changed " + maze_list[firstCoor][secondCoor] + "-> X")
    maze_list[firstCoor][secondCoor] = "X"
    print('\n'.join([str(lst) for lst in maze_list]))
    print('\n')
    statement = "\nChanged coordinate to X"
    return statement

# [4] 6.1 Check when changing Coordinate to X
def CheckForChangeX(maze_list, first, second):
    item = maze_list[first][second]
    #when the chosen change is a start/end point
    if(item == "A" or item == "B"):
        if(item == "A"):
            #Look for the nearest O and finding nearest to change to start point
            #Check if left of A is O
            if(maze_list[first][second-1] == "O"):
                CheckAroundItem(first, second - 1, "X", "A", maze_list)
            #Check if top of A is O
            elif(maze_list[first-1][second] == "O"):
                CheckAroundItem(first-1, second, "X", "A", maze_list)
            #Check if right of A is O
            elif(maze_list[first][second+1] == "O"):
                CheckAroundItem(first, second + 1, "X", "A", maze_list)
            #Check if bot of A is O
            elif(maze_list[first+1][second] == "O"):
                CheckAroundItem(first+1, second, "X", "A", maze_list)
            return "\nThe selected coordinate start point has been changed"
        else:
            #Look for the nearest O and finding nearest to change to start point
            #Check if left of B is O
            if(maze_list[first][second-1] == "O"):
                CheckAroundItem(first, second - 1, "X", "B", maze_list)
            #Check if top of B is O
            elif(maze_list[first-1][second] == "O"):
                CheckAroundItem(first-1, second, "X", "B", maze_list)
            #Check if right of B is O
            elif(maze_list[first][second+1] == "O"):
                CheckAroundItem(first, second + 1, "X", "B", maze_list)
            #Check if bot of B is O
            elif(maze_list[first+1][second] == "O"):
                CheckAroundItem(first+1, second + 1, "X", "B", maze_list)
            return "\nThe selected coordinate end point has been changed"

# [4] 7 Change Coordinate to O
def ChangeCoordToO(maze_list, coor):
    firstCoor = int(coor[0]) - 1
    secondCoor = int(coor[-1]) - 1
    print(CheckForChangeO(maze_list, firstCoor, secondCoor))
    print("Changed " + maze_list[firstCoor][secondCoor] + "-> O")
    maze_list[firstCoor][secondCoor] = "O"
    print('\n'.join([str(lst) for lst in maze_list]))
    print('\n')
    statement = "\nChanged coordinate to O"
    return statement

# [4] 7.1 Check when changing Coordinate to O
def CheckForChangeO(maze_list, first, second):
    item = maze_list[first][second]
    #when the chosen change is a start/end point
    if(item == "A" or item == "B"):
        if(item == "A"):
            #Change the nearest X to start point
            CheckAroundItem(first, second, "X", "A", maze_list)
            return "\nThe selected coordinate start point has been changed"
        else:
            #Change the nearest X to end point
            CheckAroundItem(first, second, "X", "B", maze_list)
            return "\nThe selected coordinate end point has been changed"

# [4] 8 Change Coordinate to A
def ChangeCoordToA(maze_list, coor):
    firstCoor = int(coor[0]) - 1
    secondCoor = int(coor[-1]) - 1
    print(CheckForChangeA(maze_list, firstCoor, secondCoor))
    print("Changed " + maze_list[firstCoor][secondCoor] + "-> A")
    maze_list[firstCoor][secondCoor] = "A"
    print('\n'.join([str(lst) for lst in maze_list]))
    print('\n')
    statement = "\nChanged coordinate to A"
    return statement

# [4] 8.1 Check when changing Coordinate to A
def CheckForChangeA(maze_list, first, second):
    item = maze_list[first][second]
    if(item == "A"):
        return "\n That is already your start point"
    elif(item == "B"):
        for row in maze_list:
            if("A" in row):
                #Change the original A to B if B is changed to A
                index = str(maze_list.index(row)) + ", " + str(row.index("A"))
                maze_list[int(index[0])][int(index[-1])] = "B"
                return "\n Your end point and start point exchanged places!"
        
        
# [4] 9 Change Coordinate to B
def ChangeCoordToB(maze_list, coor):
    firstCoor = int(coor[0]) - 1
    secondCoor = int(coor[-1]) - 1
    print(CheckForChangeB(maze_list, firstCoor, secondCoor))
    print("Changed " + maze_list[firstCoor][secondCoor] + "-> B")
    maze_list[firstCoor][secondCoor] = "B"
    print('\n'.join([str(lst) for lst in maze_list]))
    print('\n')
    statement = "\nChanged coordinate to B"
    return statement

# [4] 9.1 Check when changing Coordinate to B
def CheckForChangeB(maze_list, first, second):
    item = maze_list[first][second]
    if(item == "B"):
        return "\n That is already your end point"
    elif(item == "A"):
        for row in maze_list:
            if("B" in row):
                #Change the original A to B if B is changed to A
                index = str(maze_list.index(row)) + ", " + str(row.index("B"))
                maze_list[int(index[0])][int(index[-1])] = "A"
                return "\n Your end point and start point exchanged places!"

# [4] 10 Check option == 1, 2, 3, 4
def CheckOption(opt):
    value = int(opt)
    if(value <=4 and value > 0): 
        return True
    else:
        return False

# [4] 11 Check around item
def CheckAroundItem(first, second, itemCheck, itemChange, maze_list):
    if(maze_list[first-1][second] == itemCheck):
        maze_list[first-1][second] = itemChange
        return True
    elif(maze_list[first][second-1] == itemCheck):
        maze_list[first][second-1] = itemChange
        return True
    elif(maze_list[first][second+1] == itemCheck):
        maze_list[first][second+1] = itemChange
        return True
    elif(maze_list[first+1][second] == itemCheck):
        maze_list[first+1][second] = itemChange
        return True


#############################################################################################################################

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
                play_game(maze_list)
                return play_game(maze_list)
            elif option == 4:
                configure_maze()
            elif option == 0:
                print ("Thanks for playing Maze!")
                break
                return False
            else:
                print ("Invalid option. Please try again!")
        else:
            print ("Invalid option. Please try again!")
            
        print()

# TODO: For some reason there is an error when you try to run the main() function
# Additionally, since some functions for configure maze require a callback to main(maze_list)
# They are commented as well
main(maze_list)