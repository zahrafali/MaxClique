# This program uses a dictionary data structure for the graph

import math
# from icecream import ic
import sys
sys.path.append('../')
from Util.compAB_1 import *
from Util.convert_1 import *
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
graph = {}

OptClique = []

def Si(i, v):
  return v[i:n]

def clique(U, size):
  global max_, c, found, X, OptClique
  global backtrack
  backtrack = backtrack+1
  if U == None or len(U) == 0:
    if size > max_:
      max_ = size
      OptClique = X.copy()
      found = True
    return
  
  while len(U) != 0:
    if size + len(U) <= max_:
      return
    #assuming vertices start from 1 ... n
    i = min(U)-1
    if size + c[i] <= max_:
      return
    U.remove(v[i])
    X[size] = v[i]
    
    if U == None or len(U) == 0:
      clique([], size+1)
    else:
      clique(compAB(v[i], U, graph), size+1)
    if found == True:
      return
  return
 

if __name__=='__main__':
  max_ = 0
  found = False
  string_edges = open('./graphs/samp.txt', 'r').read()

  v = 0
  
  no_of_vertices = 0
  #preprocess
  processed_graph = Convert(string_edges)
  graph = processed_graph['graph']
  no_of_vertices = processed_graph['no_of_vertices']
  n = no_of_vertices
  v = list(range(1, n+1))
  c=[[0]]*(n)
  X = [0]*(n)
  for i in range(n-1, -1, -1):
    found = False
    X[0] = i+1
    clique(compAB(v[i], Si(i, v), graph), 1)
    c[i] = max_
  print("\nTime taken to execute - %s seconds\n" % (time.time() - start_time))
  while OptClique[-1] == 0:
        OptClique.pop()
  print("Clique size - ", len(OptClique))
  print("Max Clique - ", OptClique)
  print("Backtracking nodes - ", backtrack)
  
  
