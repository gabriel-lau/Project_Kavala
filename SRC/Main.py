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
def configure_maze():
    return True
