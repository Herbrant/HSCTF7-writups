class GFG: 
      
    def __init__(self): 
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1],  
                    [1, -1], [-1, -1], [-1, 1], 
                    [0, 1], [0, -1]] 
                      
    # This function searches in all 8-direction  
    # from point(row, col) in grid[][] 
    def search2D(self, grid, row, col, word): 
          
        # If first character of word doesn't match  
        # with the given starting point in grid. 
        if grid[row][col] != word[0]: 
            return False
              
        # Search word in all 8 directions  
        # starting from (row, col) 
        for x, y in self.dir: 
              
            # Initialize starting point  
            # for current direction 
            rd, cd = row + x, col + y 
            flag = True
              
            # First character is already checked,  
            # match remaining characters 
            for k in range(1, len(word)): 
                  
                # If out of bound or not matched, break 
                if (0 <= rd <self.R and 
                    0 <= cd < self.C and 
                    word[k] == grid[rd][cd]): 
                      
                    # Moving in particular direction 
                    rd += x 
                    cd += y 
                else: 
                    flag = False
                    break
              
            # If all character matched, then  
            # value of flag must be false         
            if flag: 
                return True
        return False
          
    # Searches given word in a given matrix 
    # in all 8 directions     
    def patternSearch(self, grid, word): 
          
        # Rows and columns in given grid 
        self.R = len(grid) 
        self.C = len(grid[0]) 
          
        # Consider every point as starting point  
        # and search given word 
        for row in range(self.R): 
            for col in range(self.C): 
                if self.search2D(grid, row, col, word): 
                    return row, col
    def findFlag(self, grid, x, y):
        self.R = len(grid)
        self.C = len(grid[0])

        result = ""
        col = y

        for row in range(x, -1, +1):
            if col > self.C - 1:
                break
            result = result + grid[row][col]
            col = col+1

        return result

# Driver Code 
if __name__=='__main__':
    file = open("reversed.txt", "r").readlines()

    grid = []

    for line in file:
        temp = line.replace("\n", "")
        grid.append(temp)

    gfg = GFG() 
    x, y = gfg.patternSearch(grid, '01100110011011000110000101100111') 
    print('x:{} y:{}'.format(x, y))
    result = gfg.findFlag(grid, x, y)
    print(result)

