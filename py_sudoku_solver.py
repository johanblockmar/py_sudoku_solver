
xSize = 9
xDiv = 3
ySize = 9
yDiv = 3

mainGrid = [[0 for x in range(xSize)] for y in range(ySize)] 

testString = "5,3,0,0,7,0,0,0,0\n6,0,0,1,9,5,0,0,0\n0,9,8,0,0,0,0,6,0\n8,0,0,0,6,0,0,0,3\n4,0,0,8,0,3,0,0,1\n7,0,0,0,2,0,0,0,6\n0,6,0,0,0,0,2,8,0\n0,0,0,4,1,9,0,0,5\n0,0,0,0,8,0,0,7,9"

'''
Print grid in the look of a sudoku.
grid: matrix to print.
divX: width of sudoku sub areas.
divY: height of sudoku sub areas.
'''
def prettyPrintGrid(grid, divX, divY):
    for y in range(len(grid)):
        if(y%divY==0):
            print("")

        lineStr = ""
        for x in range(len(grid[0])):
            if(x%divX==0):
                lineStr+=" "
            
            if(grid[y][x] != 0):
                lineStr += str(grid[y][x]) + " "
            else:
                lineStr += "_ "

        print(lineStr)

def CheckSudokuLine(line, sizeX):
    if(len(line) != 2 * sizeX - 1):
        return False

    return True


def enterSudoku(sizeX, sizeY, sudokuString = None):

    grid = [[0 for x in range(sizeX)] for y in range(sizeY)] 
    
    if(sudokuString == None):
        sudokuString = ""

        print("Please enter the sudoku, line by line.")
        print("Each character should be seperated by a \",\"")
        print("Please use \"0\" for the empty spaces.")
        print("Write \"q\" to exit.\n")

        for y in range(len(grid)):
            done = False
            while(not done):
                print("Please enter line {} of the sudoku".format(y+1))
                line = input()
                if(line == 'q'):
                    return None

                if(CheckSudokuLine(line,sizeX)):
                    sudokuString += line
                    if(y < len(grid)-1):
                        sudokuString += "\n"
                    done = True
                else:
                    print("Invalid, try again")

    # Parse string
    lines = sudokuString.split("\n")
    
    if(len(lines) != sizeY):
        return None
    
    for y in range(len(grid)):
        l = lines[y].split(',')
        for x in range(len(l)):
            grid[y][x] = int(l[x])

    return grid

def main():
    print("Welcome to the Sudoku Solver.\n")

    grid = enterSudoku(xSize,ySize,testString)
    if (grid == None):
        return

    mainGrid = grid

    prettyPrintGrid(mainGrid, xDiv, yDiv)
    
if __name__ == "__main__":
    main()

    input()