
import time

X_SIZE = 9
X_DIV = 3
Y_SIZE = 9
Y_DIV = 3

MAIN_GRID = [[0 for x in range(X_SIZE)] for y in range(Y_SIZE)]

TEST_STRING = (
    "5,3,0,0,7,0,0,0,0\n"
    "6,0,0,1,9,5,0,0,0\n"
    "0,9,8,0,0,0,0,6,0\n"
    "8,0,0,0,6,0,0,0,3\n"
    "4,0,0,8,0,3,0,0,1\n"
    "7,0,0,0,2,0,0,0,6\n"
    "0,6,0,0,0,0,2,8,0\n"
    "0,0,0,4,1,9,0,0,5\n"
    "0,0,0,0,8,0,0,7,9"
)

'''
Print grid in the look of a sudoku.
grid: matrix to print.
divX: width of sudoku sub areas.
divY: height of sudoku sub areas.
'''
def pretty_print_grid(grid, divx, divy):
    for y in range(len(grid)):
        if y % divy == 0:
            print("")

        line_string = ""
        for x in range(len(grid[0])):
            if x % divx == 0:
                line_string += " "

            if grid[y][x] != 0:
                line_string += str(grid[y][x]) + " "
            else:
                line_string += "_ "

        print(line_string)

def check_sudoku_line(line, size_x):
    if len(line) != 2 * size_x - 1:
        return False

    return True


def enter_sudoku(size_x, size_y, sudoku_string=None):

    grid = [[0 for x in range(size_x)] for y in range(size_y)]

    if sudoku_string is None:
        sudoku_string = ""

        print("Please enter the sudoku, line by line.")
        print("Each character should be seperated by a \",\"")
        print("Please use \"0\" for the empty spaces.")
        print("Write \"q\" to exit.\n")

        for y in range(len(grid)):
            done = False
            while not done:
                print("Please enter line {} of the sudoku".format(y+1))
                line = input()
                if line == 'q':
                    return None

                if check_sudoku_line(line, size_x):
                    sudoku_string += line
                    if y < len(grid)-1:
                        sudoku_string += "\n"
                    done = True
                else:
                    print("Invalid, try again")

    # Parse string
    lines = sudoku_string.split("\n")

    if len(lines) != size_y:
        return None

    for y in range(len(grid)):
        l = lines[y].split(',')
        for x in range(len(l)):
            grid[y][x] = int(l[x])

    return grid

def get_line_numbers(grid, y):
    line_numbers = []
    for i in range(len(grid[y])):
        if grid[y][i] != 0:
            line_numbers.append(grid[y][i])

    return line_numbers

def get_column_numbers(grid, x):
    column_numbers = []

    for j in range(len(grid)):
        if grid[j][x] != 0:
            column_numbers.append(grid[j][x])

    return column_numbers

def get_square_numbers(grid, x, y, div_x, div_y):
    square_numbers = []

    square_x_min = div_x * int(float(x) / div_x)
    square_x_max = square_x_min + div_x
    square_y_min = div_y * int(float(y) / div_y)
    square_y_max = square_y_min + div_y

    for j in range(square_y_min, square_y_max):
        for i in range(square_x_min, square_x_max):
            if grid[j][i] != 0:
                square_numbers.append(grid[j][i])

    return square_numbers


def main():
    print("Welcome to the Sudoku Solver.\n")

    grid = enter_sudoku(X_SIZE, Y_SIZE, TEST_STRING)
    if grid is None:
        return

    passes = 0
    done = False

    start = time.time()
    while not done:
        done = True
        passes += 1
        pretty_print_grid(grid, X_DIV, Y_DIV)
        print("-----------------------")

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    done = False
                    ln = get_line_numbers(grid, y)
                    cn = get_column_numbers(grid, x)
                    sn = get_square_numbers(grid, x, y, X_DIV, Y_DIV)

                    numbers = ln + cn + sn
                    numbers = sorted(numbers)

                    possible = []
                    for i in range(1, 10):
                        if i not in numbers:
                            possible.append(i)

                    if len(possible) == 1:
                        grid[y][x] = possible[0]

    print("Solved in {} passes.\nTime: {} ms".format(passes, (time.time()-start)*1000))

if __name__ == "__main__":
    main()

    #input()
