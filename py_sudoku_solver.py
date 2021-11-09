
xSize = 9
xDiv = 3
ySize = 9
yDiv = 3

mainGrid = [[0 for x in range(xSize)] for y in range(ySize)] 

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
            
            lineStr += str(grid[x][y]) + " "

        print(lineStr)

def main():
    prettyPrintGrid(mainGrid, xDiv, yDiv)
    
if __name__ == "__main__":
    main()

    input()