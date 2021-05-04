import math
from Util.graph_edges import *
import sys
sys.path.append('../')
from Util.compAB import *
import time
start_time = time.time()

backtrack = 0
OptSize = 0
OptClique = []
X = []
C = []
n = 0
graph = []
AnB = []
prob_max_cli = 0

def maxCliques(l):
  global backtrack
  backtrack = backtrack+1
  global OptSize, X, OptClique
  
  if l > OptSize:
    OptSize = l
    OptClique = X.copy()
  
  if l > 0:
    # remove append, add in specific location, do initial array initialization
    C[l] = compAB(X[l-1], C[l-1], graph)

  # adding bounding
  M = l + len(C[l])  
  for i in C[l]:
    if M <= OptSize:
      # print("bound", M)
      return
    X[l]=i
    maxCliques(l+1)
    # do not erase the values of X, you can save the partial solution
    
    
  return
  

if __name__=='__main__':
  OptSize = 0
  # code_len = n (as given in assignment)
  code_len = 7
  dist = 4
  n =  int(math.pow(2,code_len))
  print(n)
  edges = gEdges(code_len, dist)
  # print(edges)
  V = [i for i in range(0, n)]
  C=[0]*(n)
  C[0] = V
  v1 = 0
  v2 =0
  X = [0]*(n)
  # creating an adjacency matrix for the graph
  graph = [[0 for i in range(n)] for j in range(n)]
  
  for i in edges:
    # print(i)
    v1 = i[0]
    v2 = i[1]
    graph[v1][v2] = 1
    graph[v2][v1] = 1
  # print(graph)

  #getting A[0] for C[1]
  # C[1] = []
  # A0 = graph[0]
  # for i, val in enumerate(A0):
  #   if val ==1:
  #     C[1].append(i)
  # make sure the first node is zero, x[0] = 0000 
  # make c[1] = neighbors of zero
  # call maxclique with l =1
  # n=7 8355(without bound), lesser(with bound), to verify
  maxCliques(0)
  print("\nTime taken to execute - %s seconds\n" % (time.time() - start_time))
  print("n = ", code_len)
  print("d = ", dist)
  print("A(n, 4) = ",OptSize)
  bit = '0'+str(code_len)+'b'
  OptClique = {format(i, bit) for i in OptClique }
  print("Codes - ", OptClique)
  print("Backtracking nodes = ", backtrack)
  

  
  
