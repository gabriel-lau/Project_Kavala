
# Load maze from maze foler
def ReadLoadMaze():
    print("Option [1] Read and load maze from file")

def ViewMaze():
    print("Option [2] View Maze")

def PlayMaze():
    print("Option [3] Play maze game")

def ConfigureMaze():
    print("Option [4] Configure current maze")

while True:
    print(
        """

        MAIN MENU
        =========
        [1] Read and load maze from file
        [2] View Maze
        [3] Play maze game
        [4] Configure current maze

        [0]    Exit Maze

        """)
    choice = input("Enter your option: ")
    choice = str(choice)
    
    if choice == "1":
        ReadLoadMaze()
    elif choice == "2":
        ViewMaze()
    elif choice == "3":
        PlayMaze()
    elif choice == "4":
        ConfigureMaze()
    elif choice == "5":
        break

    else:
        print("Invalid Input")
        continue

