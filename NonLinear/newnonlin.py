import math
from Util.hamming_distance import *
from Util.graph_edges import *
import time
start_time = time.time()

backtrack = 0
max_ = 0
S = []
found = False
c = []
v = []
n = 0
X = []
graph = []

OptClique = [] 

def compAB(vertex, C_prev):
  global graph
  AnB = []
  for i in C_prev:
    if graph[vertex][i] == 1: #and i > vertex:
      AnB.append(i)
  return AnB

def Si(i, v):
  return v[i:n]

def clique(U, size):
  global backtrack
  backtrack = backtrack+1
  global max_, c, found, X, OptClique
  if U == None or len(U) == 0:
    if size > max_:
      max_ = size
      OptClique = X.copy()
      found = True
    return
  
  while len(U) != 0:
    if size + len(U) <= max_:
      return
    #assuming vertices start from 0 ... n
    i = U[0]#min(U)
    if size + c[i] <= max_:
      return
    U.remove(v[i])
    X[size] = v[i]
    if U == None or len(U) == 0:
      clique([], size+1)
    else:
      clique(compAB(v[i], U), size+1)
    if found == True:
      return
  
  return

if __name__=='__main__':
  max_ = 0
  found = False
  code_len = 7
  dist = 4
  n =  int(math.pow(2,code_len))
  print(n)
  edges = gEdges(code_len, dist)
  v = [i for i in range(0, n)]
  # edges = [[0,1], [0,2], [1,2], [1,3], [1,4], [2,3], [2,4], [2,5], [3,4], [3,5], [4,5]]
  # creating an adjacency matrix for the graph
  graph = [[0 for i in range(n)] for j in range(n)]
  for i in edges:
    v1 = i[0]
    v2 = i[1]
    graph[v1][v2] = 1
    graph[v2][v1] = 1
  c=[[0]]*(n)
  X = [0]*(n)
  for i in range(n-1, -1, -1):
    found = False
    X[0] = i
    clique(compAB(v[i], Si(i, v)), 1)
    c[i] = max_
  print("\nTime taken to execute - %s seconds\n" % (time.time() - start_time))
  print("n = ", code_len)
  print("d = ", dist)
  # print("Max Clique = ",OptClique)
  while OptClique[-1] == 0:
        OptClique.pop()
  print("A(n, 4) = ", max_)
  bit = '0'+str(code_len)+'b'
  OptClique = {format(i, bit) for i in OptClique }
  print("Codes - ", OptClique)
  print("Backtracking nodes = ", backtrack)

  