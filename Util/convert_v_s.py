# This function supports dictionary data structure and vertex ordering
# Preprocess input, convert string to integer list
def Convert(string, ascending): 
  details = string
  details = details.partition('\n')[0]
  details = list(details.split(" "))
  # no_of_edges = details[0]
  no_of_vertices = int(details[1])
  li = list(string.splitlines()[1:])
  
  #graph would look like
  #   graph: {1: {'adj': [0, 1, 0, 0, 0, 0, 1], 'order': 2},
  #           2: {'adj': [1, 0, 1, 0, 0, 1, 1], 'order': 4},
  #           3: {'adj': [0, 1, 0, 1, 1, 0, 0], 'order': 3},
  #           4: {'adj': [0, 0, 1, 0, 1, 0, 0], 'order': 2},
  #           5: {'adj': [0, 0, 1, 1, 0, 0, 0], 'order': 2},
  #           6: {'adj': [0, 1, 0, 0, 0, 0, 1], 'order': 2},
  #           7: {'adj': [1, 1, 0, 0, 0, 1, 0], 'order': 3}}
  graph = { i : { 'adj': [0]*(no_of_vertices)} for i in range(1, no_of_vertices+1) }
  vertices = { i: 0 for i in range(1, no_of_vertices+1)}
  for i in li:
    i = i.strip()
    e_0 = 0
    count = 0
    for j in i.split(" "):
      #incrementing to get the order of the vertex
      # graph[int(j)]["order"] = graph[int(j)]["order"]+1
      vertices[int(j)] = vertices[int(j)]+1
      if count == 0:
        e_0 = int(j)
      else:
        # getting the adjacency matrix
        graph[int(j)]["adj"][e_0-1] = 1
        graph[e_0]["adj"][int(j)-1] = 1
      count = count + 1
  sorted_vertices =[ k for k, v in sorted(vertices.items(), key=lambda x: x[1], reverse=ascending)]
  # print(sorted_vertices)
  return {'graph' : graph, 'no_of_vertices': no_of_vertices, 'vertices': sorted_vertices}
