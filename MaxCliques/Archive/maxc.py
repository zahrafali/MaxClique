# This program uses a list data structure for the graph

import math
import sys
sys.path.append('../')
from Util.compAB import *
from Util.convert import *
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
    #remove 0s
    # OptClique = [i for i in OptClique if i != 0]
  if l > 0:
    # check append, add in specific location, do initial array initialization
    C[l]=(compAB(X[l-1], C[l-1], graph))
  # adding bounding
  M = l + len(C[l]) 
  
  for i in C[l]:
    if M <= OptSize:
      # print("**")
      return
    # print(X, l)
    X[l]=i
    maxCliques(l+1)
  
    # do not erase the values of X, you can save the partial solution
    # X = [0]*(n)
    # X = []
  return
  

if __name__=='__main__':
  OptSize = 0
  
  # test files
  string_edges = open('./graphs/c-fat/c-fat500-2.clq', 'r').read()
  V = 0
  edges = []
  no_of_vertices = 0
  processed_graph = Convert(string_edges)
  edges = processed_graph['edges']
  no_of_vertices = processed_graph['no_of_vertices']
  n = no_of_vertices
  V = list(range(1, no_of_vertices+1))

  # V = [i for i in range(0, n)]
  C=[0]*(n)
  C[0] = V
  v1 = 0
  v2 =0
  X = [0]*(n)
  
  # creating an adjacency matrix for the graph
  graph = [[0 for i in range(n)] for j in range(n)]
  for i in edges:
    v1 = i[0]
    v2 = i[1]
    graph[v1-1][v2-1] = 1
    graph[v2-1][v1-1] = 1
  # graph = [[0,1], [0,3], [0,6], [1,2], [1,4], [1,5], [2,3], [2,4], [2,5], [3,6]]

  maxCliques(0)
  print("\nTime taken to execute - %s seconds\n" % (time.time() - start_time))
  print("A(n, 4) = ",OptSize)
  while OptClique[-1] == 0:
        OptClique.pop()
  print("Clique - ", OptClique)
  # for i,val in enumerate(OptClique):
  #   if val!=0:
  #     print(i)
  print("Backtracking nodes = ", backtrack)

  

  
  
