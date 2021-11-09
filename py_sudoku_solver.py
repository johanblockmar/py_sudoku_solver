
xSize = 9
ySize = 9

mainGrid = [[0 for x in range(xSize)] for y in range(ySize)] 

def prettyPrintGrid(grid):
    for y in range(len(grid)):
        print(grid[y])

def main():
    prettyPrintGrid(mainGrid)
    
if __name__ == "__main__":
    main()

    input()