from icecream import ic
# a = {
#   'b':[1,3,5,2,7]
# }

# print(a['b'][2])

d = {'one':1,'three':3,'five':5,'two':2,'four':4}
a ={k: v for k, v in sorted(d.items(), key=lambda x: x[1])}
print(a)

graph = {1: {'adj': [0, 1, 0, 0, 0, 0, 1], 'order': 2},
        2: {'adj': [1, 0, 1, 0, 0, 1, 1], 'order': 4},
        3: {'adj': [0, 1, 0, 1, 1, 0, 0], 'order': 3},
        4: {'adj': [0, 0, 1, 0, 1, 0, 0], 'order': 2},
        5: {'adj': [0, 0, 1, 1, 0, 0, 0], 'order': 2},
        6: {'adj': [0, 1, 0, 0, 0, 0, 1], 'order': 2},
        7: {'adj': [1, 1, 0, 0, 0, 1, 0], 'order': 3}}
l ={k: v for k, v in sorted(graph.items(), key=lambda k_v: k_v[1]['order'])}
print(l)