"""
leetcode 419
"""

def countBattleships(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    SHIP_CHAR = 'X'
    battleshipCount = 0

    def isValid(position, board):
      y, x = position
      return (
        y > -1 and
        y < len(board) and
        x > -1 and
        x < len(board[y])
      )

    def walkShip(position, board):
      y, x = position
      if isValid(position, board) and board[y][x] == SHIP_CHAR:
        board[y][x] = '.'
        # go up
        walkShip((y-1, x), board)
        # go down
        walkShip((y+1, x), board)
        # go left
        walkShip((y, x-1), board)
        # go right
        walkShip((y, x+1), board)


    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == SHIP_CHAR:
          battleshipCount += 1
          walkShip((i, j), board)

    return battleshipCount
