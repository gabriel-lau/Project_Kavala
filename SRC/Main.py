# Display main menu (and allow for repetition)
# while True:

def displayMenu():
    menu = ("MAIN MENU\n" 
            "=========\n"
            "[1] Read and load maze from file\n"
            "[2] View maze\n"
            "[3] Play maze game\n"
            "[4] Configure current maze\n\n"
            "[0] Exit Maze\n")

    print(menu)
    return menu