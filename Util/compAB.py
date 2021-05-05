def compAB(vertex, C_prev, graph):
  
  # global graph
  AnB = []
  # no need to intersect after, check in c prev in here, check for element in cPrev
  for i in C_prev:
    if graph[vertex-1][i-1] == 1 and i > vertex:
      # print(vertex, C_prev, i)
      AnB.append(i)
  # This calculates the value of A n B n C[l-1] (formula)
  # can elemintate this step
  # AnB = sorted(list(set(AnB).intersection(set(C_prev))))
  return AnB