import random
from time import sleep
from time import time

n = 3

def create_board():

    board = [
    [ '_', '_', '_' ], 
    [ '_', '_', '_' ], 
    [ '_', '_', '_' ]]

    return board


def possibilities(board):
    l = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == '_':
                l.append((i, j))
    return l


def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    x,y = current_loc
    board[x][y] = player
    return(board)

def row_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x][y] != player:
                win = False
                continue

        if win == True:
            return(win)
    return(win)

def col_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue

        if win == True:
            return(win)
    return(win)

def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x][x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x][y] != player:
                win = False
    return win

def evaluate(board):
    winner = 'no'

    for player in ['x', 'o']:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player

    if (not isMovesLeft(board)) and winner == 'no':
        winner = 'tie'
    return winner

def printMatrix(mat):

  for i in range(n):
      for j in range(n):
          print("%s " % (mat[i][j]), end = " ")

      print()

def isMovesLeft(b):
  for i in b:
    if '_' in i:
      return True

  return False

def play_game():
  board, winner, counter = create_board(), 'no', 1
  printMatrix(board)
  sleep(1)
  player = 'x'

  while winner == 'no':
    if (player == 'x'):
      board = random_place(board, player)
      print("\nBoard after " + str(counter) + " move")
      printMatrix(board)
      sleep(1)
      counter += 1
      winner = evaluate(board)
      if winner != 'no':
        break
      else:
        player = 'o'
    else:
      pos = input("input number: ")
      (i,j) = tuple(map(int, pos.split(' ')))
      while board[i][j] !='_':
        pos = input("input number: ")
        (i,j) = tuple(map(int, pos.split(' ')))

      board[i][j] = player
      print("\nBoard after " + str(counter) + " move")
      printMatrix(board)
      sleep(2)
      counter += 1
      winner = evaluate(board)
      if winner != 'no':
        break
      else:
        player = 'x'
  return(winner)

print("Winner is: " + str(play_game()))
