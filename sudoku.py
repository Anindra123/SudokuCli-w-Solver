import copy
from math import floor


def printGrid(grid):
    print("   ", end="")
    for i in range(0, 1):
        count = 0
        for j in range(0, 9):
            count += 1
            if count == 3:
                print(j, end=" ")
                count = 0
            else:
                print(j, end=" ")
    print("\n  -------------------")
    c = 0
    for i in range(0, len(grid)):
        count = 0
        print(f"{i} |", end="")
        for j in range(0, len(grid[0])):
            count += 1
            if count == 3:
                print(grid[i][j], end="|")
                count = 0
            else:
                print(grid[i][j], end=" ")
        c += 1
        if c == 3:
            print("\n  -------------------")
            c = 0
        else:
            print()


def solved(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 0:
                return False

    return True


def valid_move(grid, row, col, num):
    flag = True

    # check whether the value is placed in a empty cell
    if grid[row][col] != 0:
        flag = False

    # checks whether duplicate value placed in current coloumn
    for c in range(0, 9):
        if grid[row][c] == num:
            flag = False

    # checks whether duplicate value placed in current row
    for r in range(0, 9):
        if grid[r][col] == num:
            flag = False

    # top most and left most row and coloumn
    n_r = floor(row/3)*3
    n_c = floor(col/3)*3

    # checks whether duplicate value in current 3x3 grid
    for i in range(n_r, n_r+3):
        for j in range(n_c, n_c+3):
            if grid[i][j] == num:
                flag = False
    return flag


def validate_pos(pos):

    if len(pos) != 3:
        return False

    if pos.__contains__(",") is False:
        return False

    pos.split(",")
    row = pos[0]
    col = pos[2]
    if row.isdigit() is False and col.isdigit() is False:
        return False
    if int(row) > 8 or int(row) < 0:
        return False
    if int(col) > 8 or int(col) < 0:
        return False
    return True


def valid_num(num):
    if len(num) == 0:
        return False
    if num.isdigit() is False:
        return False
    if int(num) > 9 or int(num) < 0:
        return False
    return True


def play_game(grid):

    # Main game loop
    b_grid = copy.deepcopy(grid)
    while True:
        print()
        printGrid(grid)
        print()
        print("Place a move : p")
        print("Clear a move : c")
        print("Quit : q")
        val = input(
            "\nEnter a command : ")
        if val == "q":
            break
        elif val == "p" or val == "c":
            pos = input("\nEnter a position with format \"row,col\" : ")
            if validate_pos(pos):
                pos.split(",")
                row = int(pos[0])
                col = int(pos[2])
                if val == "p":
                    num = input("\nEnter a number to place : ")
                    if valid_num(num) and valid_move(grid, row, col, int(num)):
                        grid[row][col] = int(num)
                        print(
                            f"\nMove {int(num)} placed at [{row},{col}]")
                    else:
                        print("\nNot a valid move")
                if val == "c":
                    if b_grid[row][col] == 0:
                        grid[row][col] = 0
                        print(f"\n Move cleared at [{row},{col}]")
                    else:
                        print("\nCannot clear at that position")
        else:
            print("\nNot a valid input")

        if solved(grid):
            print("\nCongratulation you solved the puzzle!\n")
            print("Final Grid")
            printGrid(grid)
            break


def recursive_backtrack_solver(grid, no_of_recursion):
    no_of_recursion += 1
    if solved(grid):
        print("\nSolved Grid\n")
        printGrid(grid)
        print(f"\n Number of recursions : {no_of_recursion}")
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 0:  # loop through each of the cells
                for n in range(1, 10):
                    if valid_move(grid, i, j, n):  # check the invalid condition of sudoku
                        grid[i][j] = n
                        # recursive call
                        if recursive_backtrack_solver(grid, no_of_recursion):
                            return True  # base case
                        else:
                            grid[i][j] = 0
                return False
    return True  # base case


def solver(grid):
    while True:
        print()
        printGrid(grid)
        print()
        val = input("Enter \"s\" to start solving or \"q\" to go back :")
        if val == "s":
            s_grid = copy.deepcopy(grid)
            output = recursive_backtrack_solver(s_grid, 0)
            if output:
                break
        elif val == "q":
            break
        else:
            print("Invalid option")


def main():
    grid = [[0, 5, 3, 2, 0, 7, 0, 0, 8],
            [6, 0, 1, 5, 0, 0, 0, 0, 2],
            [2, 0, 0, 9, 1, 3, 0, 5, 0],
            [7, 1, 4, 6, 9, 2, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 6, 0],
            [0, 0, 0, 4, 5, 1, 2, 9, 7],
            [0, 6, 0, 3, 2, 5, 0, 0, 9],
            [1, 0, 0, 0, 0, 6, 3, 0, 4],
            [8, 0, 0, 1, 0, 9, 6, 7, 0]
            ]
    while True:
        print()
        print("Welcome to Sudoku !")
        print("Play game : p")
        print("Solver : s")
        print("Quit: q")
        val = input("Enter an option :")
        if val == "p":
            play_game(grid)
        elif val == "s":
            solver(grid)
        elif val == "q":
            print("Thanks for playing")
            break
        else:
            print("Invalid option")


if __name__ == '__main__':
    main()
