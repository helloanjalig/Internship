class Node:
    def __init__(self, row, col, value):
        self.id = str(row) 
        self.row = row 
        self.col = col 
        self.value = value
        self.distanceFromStart = float('inf') # g
        self.estimatedDistancetoEnd = float('inf') # f
        self.cameFrom = None

def aStarAlgorithm(startRow, ) 