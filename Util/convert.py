# Preprocess input, convert string to integer list
def Convert(string): 
  edges = []
  # global edges, no_of_vertices, no_of_edges
  details = string
  details = details.partition('\n')[0]
  details = list(details.split(" "))
  # no_of_edges = details[0]
  no_of_vertices = int(details[1])
  li = list(string.splitlines()[1:])
  
  for i in li:
    i = i.strip()
    edge = [int(x) for x in i.split(" ")]
    edges.append(edge)
  return {'edges' : edges, 'no_of_vertices': no_of_vertices}