import math
# from icecream import ic
import sys
sys.path.append('../')
from Util.compAB import *
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

def Si(i, v):
  return v[i:n]

def clique(U, size):
  # print(U)
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
    #assuming vertices start from 0 ... n
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

# Preprocess input, convert string to integer list
def Convert(string): 
  global edges, no_of_vertices, no_of_edges
  details = string_edges
  details = details.partition('\n')[0]
  details = list(details.split(" "))
  no_of_edges = details[0]
  no_of_vertices = int(details[1])
  li = list(string.splitlines()[1:])
  
  for i in li:
    i = i.strip()
    edge = [int(x) for x in i.split(" ")]
    edges.append(edge)
  return edges 

if __name__=='__main__':
  max_ = 0
  found = False
  # creating an adjacency matrix for the graph
  # string_edges = open('./graphs/ost.txt', 'r').read()
  string_edges = open('./graphs/MANN_a9.clq', 'r').read()
  v = 0
  edges = []
  no_of_edges = 0
  no_of_vertices = 0
  str1 = string_edges
  Convert(str1)
  n = no_of_vertices
  v = list(range(1, no_of_vertices+1))
  graph = [[0 for i in range(n)] for j in range(n)]
  for i in edges:
    v1 = i[0]
    v2 = i[1]
    graph[v1-1][v2-1] = 1
    graph[v2-1][v1-1] = 1
  c=[[0]]*(n)
  X = [0]*(n)
  for i in range(n-1, -1, -1):
    found = False
    X[0] = i+1
    clique(compAB(v[i], Si(i, v), graph), 1)
    c[i] = max_
  print("\nTime taken to execute - %s seconds\n" % (time.time() - start_time))
  # print("Max Clique = ",OptClique)
  while OptClique[-1] == 0:
        OptClique.pop()
  print("Clique size - ", len(OptClique))
  print("Max Clique - ", OptClique)
  print("Backtracking nodes - ", backtrack)
  
  
