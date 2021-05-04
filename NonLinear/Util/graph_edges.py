import math
from Util.hamming_distance import *

def gEdges(n, d):
  vertices = int(math.pow(2,n))
  edges = []
  for i in range (vertices):
    for j in range(i+1, vertices):
      if hammingDistance(i,j) >= d:
        edges.append([i, j])
  return edges