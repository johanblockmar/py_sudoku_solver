
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

        lineStr = ""
        for x in range(len(grid[0])):
            if x % divx == 0:
                lineStr+=" "
            
            if grid[y][x] != 0:
                lineStr += str(grid[y][x]) + " "
            else:
                lineStr += "_ "

        print(lineStr)

def CheckSudokuLine(line, sizeX):
    if len(line) != 2 * sizeX - 1:
        return False

    return True


def enterSudoku(sizeX, sizeY, sudokuString = None):

    grid = [[0 for x in range(sizeX)] for y in range(sizeY)] 
    
    if sudokuString == None:
        sudokuString = ""

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

                if CheckSudokuLine(line,sizeX):
                    sudokuString += line
                    if y < len(grid)-1:
                        sudokuString += "\n"
                    done = True
                else:
                    print("Invalid, try again")

    # Parse string
    lines = sudokuString.split("\n")
    
    if len(lines) != sizeY:
        return None
    
    for y in range(len(grid)):
        l = lines[y].split(',')
        for x in range(len(l)):
            grid[y][x] = int(l[x])

    return grid

def getLineNumbers(grid,y):
    lineNumbers = []
    for i in range(len(grid[y])):
        if grid[y][i] != 0:
            lineNumbers.append(grid[y][i])

    return lineNumbers

def getColumnNumbers(grid,x):
    columnNumbers = []

    for j in range(len(grid)):
        if grid[j][x] != 0:
            columnNumbers.append(grid[j][x])

    return columnNumbers

def getSquareNumbers(grid, x, y, divX, divY):
    squareNumbers = []
    
    squareXmin = divX * int(float(x) / divX)
    squareXmax = squareXmin + divX
    squareYmin = divY * int(float(y) / divY)
    squareYmax = squareYmin + divY
    
    for j in range(squareYmin,squareYmax):
        for i in range(squareXmin,squareXmax):
            if grid[j][i] != 0:
                squareNumbers.append(grid[j][i])

    return squareNumbers

    

def main():
    print("Welcome to the Sudoku Solver.\n")

    grid = enterSudoku(X_SIZE,Y_SIZE,TEST_STRING)
    if grid == None:
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
                    ln = getLineNumbers(grid, y)
                    cn = getColumnNumbers(grid, x)
                    sn = getSquareNumbers(grid, x, y, X_DIV, Y_DIV)

                    numbers = ln + cn + sn
                    numbers = sorted(numbers)
                    
                    possible = []
                    for i in range(1,10):
                        if i not in numbers:
                            possible.append(i)
                    
                    if len(possible) == 1:
                        grid[y][x] = possible[0]

    print("Solved in {} passes.\nTime: {} ms".format(passes, (time.time()-start)*1000))
    
if __name__ == "__main__":
    main()

    #input()