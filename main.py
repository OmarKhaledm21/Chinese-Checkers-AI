class Game:
    def __init__(self):
        self.board = [
                                            ["G"],
                                          ["G","G"],
                                        ["G","G","G"],
                                      ["G","G","G", "G"],
                 ["B", "B", "B", "B", ".", ".", ".", ".", ".", "Y", "Y", "Y", "Y"],
                   ["B", "B", "B", ".", ".", ".", ".", ".", ".", "Y", "Y", "Y"],
                      ["B", "B", ".", ".", ".", ".", ".", ".", ".", "Y", "Y"],
                        ["B", ".", ".", ".", ".", ".", ".", ".", ".", "Y"],
                           [".", ".", ".", ".", ".", ".", ".", ".", "."],
                        ["P", ".", ".", ".", ".", ".", ".", ".", ".", "O"],
                      ["P", "P", ".", ".", ".", ".", ".", ".", ".", "O", "O"],
                   ["P", "P", "P", ".", ".", ".", ".", ".", ".", "O", "O", "O"],
                 ["P", "P", "P", "P", ".", ".", ".", ".", ".", "O", "O", "O", "O"],
                                      ["R","R","R","R"],
                                        ["R","R","R"],
                                          ["R","R"],
                                            ["R"]
        ]
        self.cols = 13
        self.rows = 17
    
      # executes a move, Note: This function assumes that the given next move is valid
    def move(self, pieceRow, pieceCol, destRow, destCol):
        self.board[destRow][destCol] = self.board[pieceRow][pieceCol]
        self.board[pieceRow][pieceCol] = "."
    
    def getAvailMoves(self, pieceRow, pieceCol):
        moves = []
        dirs = [
          [-1, -1], # north west
          [-1, 0], # north east
          [0, 1], # east
          [0, -1], # west
          [1, 0], # south west
          [1, 1] # south east
        ]
        for dir in dirs:
          newRow = pieceRow + dir[0]
          newCol = pieceCol + dir[1]
          if newRow



