import math
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

def gEdges(n, d):
  vertices = int(math.pow(2,n))
  edges = []
  for i in range (vertices):
    for j in range(i+1, vertices):
      edges.append([i+1, j+1])
  print("------")
  return edges

def compAB(vertex, C_prev):
  global graph
  AnB = []
  for i in C_prev:
    if graph[vertex][i] == 1: #and i > vertex:
      AnB.append(i)
  # print("vertex - ",vertex, "Si - ", C_prev, "Intersection value - ", AnB)
  return AnB

def Si(i, v):
  return v[i:n]

def clique(U, size):
  global max_, c, found, X, OptClique
  # print(c[n], size)
  global backtrack
  backtrack = backtrack+1
  # print(OptClique)
  if U == None or len(U) == 0:
    if size > max_:
      max_ = size
      OptClique = X.copy()

      found = True
    return
  
  
  while len(U) != 0:
    # print("size, U", size, U)
    if size + len(U) <= max_:
      # print("Size bound")
      return
    #assuming vertices start from 0 ... n
    i = min(U)
    if size + c[i] <= max_:
      # print("russian doll bound", X)
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
  # v = [0, 1, 2, 3, 4, 5, 6]
  # edges = [[0,1], [0,3], [0,6], [1,2], [1,4], [1,5], [2,3], [2,4], [2,5], [3,6]]
  # edges = [[0,1], [0,2], [1,2], [1,3], [1,4], [2,3], [2,4], [2,5], [3,4], [3,5], [4,5]]
  # creating an adjacency matrix for the graph
  # test files
  string_edges = open('./a3graphs/ostergard.txt', 'r').read()
  # string_edges = open('./a3graphs/sample1.txt', 'r').read()
  # string_edges = open('./a3graphs/graphv16_m30_mc7.txt', 'r').read()
  # string_edges = open('./a3graphs/graphv16_m60_mc5.txt', 'r').read()
  # string_edges = open('./a3graphs/graphv16_m90_mc3.txt', 'r').read()
  # string_edges = open('./a3graphs/rand_v100d30_mc6.txt', 'r').read()
  # string_edges = open('./a3graphs/rand_v100d50_mc9.txt', 'r').read()
  # string_edges = open('./a3graphs/rand_v100d70_mc15.txt', 'r').read()
  v = 0
  edges = []
  no_of_edges = 0
  no_of_vertices = 0
  str1 = string_edges
  Convert(str1)
  n = no_of_vertices
  v = list(range(0, no_of_vertices))

  graph = [[0 for i in range(n)] for j in range(n)]
  for i in edges:
    v1 = i[0]
    v2 = i[1]
    graph[v1][v2] = 1
    graph[v2][v1] = 1
  c=[[0]]*(n)
  X = [0]*(n)
  # print(graph)
  for i in range(n-1, -1, -1):
    found = False
    # print("apple--", compAB(v[i], Si(i, v)))
    X[0] = i
    # print("X--", X, Si(i, v))
    clique(compAB(v[i], Si(i, v)), 1)
    c[i] = max_
  print("\nTime taken to execute - %s seconds\n" % (time.time() - start_time))
  # print("Max Clique = ",OptClique)
  while OptClique[-1] == 0:
        OptClique.pop()
  print("refined 22- ", OptClique)
  print("Backtracking nodes = ", backtrack)

  
