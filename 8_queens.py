import copy
import numpy as np
import matplotlib.pyplot as plt

class Node:
  def __init__(self, state=None, parent=None):
    self.state = state
    self.parent = parent
    self.children = []

  def addChildren(self, children):
    self.children.extend(children)
        
def expandAndReturnChildren(node):
  children = []
  board = node.state 
  j = sum(line.count(1) for line in board) #number of queens already placed
  for i in range(0,len(board[0])):
    child = copy.deepcopy(board)
    child[j][i] = 1
    children.append(Node(child, board))
  return children

def isPossible(board):
    board = board.state
    row = sum(line.count(1) for line in board) - 1 #number of queens already placed
    for z in range(len(board)):
        if board[row][z] == 1:
            col = z         
    
    # Check this col on left side
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    # check right diagonal above
    for i, j in zip(range(row-1, -1, -1), range(col+1, (len(board)), 1) ):
        if board[i][j] == 1:
            return False
        
    # check left diagonal above
    for i, j in zip(range(row-1, -1, -1),range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    return True
    
def dfs(board):
  frontier = []
  explored = []
  found_goal = False
  goalie = Node()
  
  # add initial state to frontier
  frontier.append(Node(board, None))
  
  while not found_goal:
    # goal test
    if (sum(line.count(1) for line in frontier[0].state) == len(board)):
      found_goal = True
      goalie = frontier[0]
      break
      
    # expand the first in the frontier
    children = expandAndReturnChildren(frontier[0])
    # add children list to the expanded node
    frontier[0].addChildren(children)
    # add to the explored list
    explored.append(frontier[0])
    # remove the expanded frontier
    del frontier[0]
    # add children to the frontier
    index = 0
    for child in children:
        if isPossible(child):
            frontier.insert(index,child)
            index = index + 1
  
  solution = goalie.state

  return solution

def drawChessboard(solution):
    # print the solution as characters in the console
    print("1 represents a queen | 0 represents an empty space\n")
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in solution]))
    
    # create the chessboard and display it with matplotlib
    plt.figure(figsize=(len(solution),len(solution)))
    plt.title("Solution for %i queens on a %i x %i chessboard" %(N, N, N))
    chessboard = np.zeros((len(solution),len(solution)))
    chessboard[1::2,0::2] = 1
    chessboard[0::2,1::2] = 1
    plt.imshow(chessboard, cmap='binary')
    
    # hide figure axises
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # plot the queens from the solution onto the chessboard
    for i in range(len(solution)):
        for j in range(len(solution)):
            if solution[j][i] == 1:
                plt.text(i, j, '\u265b', fontsize=30, ha='center', va='center', color='black' if (i - j) % 2 == 0 else 'white')
    plt.show()

if __name__ == "__main__":
  print("\n=== Solving N-Queen Problem using the DFS Search Algorithm ===")
  print("\n" + "-"*90 + "\nSolution:\n")
  N = int(input("Enter number of queens (minimum 4): "))
  while N < 4:
      print("Number of queens must be at least 4.")
      N = int(input("Enter number of queens: "))
      
  board = [[0 for i in range(N)] for j in range(N)]
  solution = dfs(board)
  drawChessboard(solution)