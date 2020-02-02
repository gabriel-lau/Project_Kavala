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


# [1] Read and load file
def read_file(maze_list):
    print ("Option [1]: Read and load maze from file")
    print ("==========================================")
    filename = input("Enter the name of the data file: ")

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
# ../maze.csv
def play_game(maze_list):
    for list in maze_list:
        for index, list in enumerate(maze_list):
            if 'A' in list:
                row_A = index + 1
                column_A = maze_list[index].index('A') + 1
            if 'B' in list:
                row_B = index + 1
                column_B = maze_list[index].index('B') + 1
                break

    if maze_list == []:
        print("No maze in memory. Load your maze file through Option 1!")
    else:    
        print ("Option [3]: Play maze game")
        print ("==========================================")
        print('\n'.join([str(lst) for lst in maze_list]))
        print('\n''Location of Start (A) = ' + '(Row ' + str(row_A) + ', Column ' + str(column_A) +')') # Printing out location
        print('\n''Location of Start (B) = ' + '(Row ' + str(row_B) + ', Column ' + str(column_B) +')')
        return False # Comment this line to run the game
        movement = input(str('\n'"Press 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MAIN MENU: ")) # Movement code
        if movement == 'M':
            print("movement is M")
            return main(maze_list)
        elif movement == 'W':
            print("movement is W")
            return play_game(maze_list)
        elif movement == 'A':
            print("movement is A")
            return play_game(maze_list)
        elif movement == 'S':
            print("movement is S")
            return play_game(maze_list)
        elif movement == 'D':
            print("movement is D")
            return play_game(maze_list)
        else:
        #if movement != 'W' or 'A' or 'S' or 'D' or 'M':
            print("Invalid Character. Please try again!")
            print ("HI")
            return play_game(maze_list)
            #return movement 

    return maze_list


# [4] Configure maze
def configure_maze():
    return True


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
                return False
            else:
                print ("Invalid option. Please try again!")
        else:
            print ("Invalid option. Please try again!")
            
        print()

# TODO: For some reason there is an error when you try to run the main() function!!!
#main(maze_list)