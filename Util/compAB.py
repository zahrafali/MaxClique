def compAB(vertex, C_prev, graph):
  # global graph
  AnB = []
  # no need to intersect after, check in c prev in here, check for element in cPrev
  for i in C_prev:
    if graph[vertex][i] == 1 and i > vertex:
      AnB.append(i)
  # This calculates the value of A n B n C[l-1] (formula)
  # can elemintate this step
  # AnB = sorted(list(set(AnB).intersection(set(C_prev))))
  return AnB