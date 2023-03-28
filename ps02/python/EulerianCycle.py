from random import randint
from copy import deepcopy

def CreateAdjacencyList2(g_text_rep):
    
    adj_list = {}
    circuit_max = 0
    lines = [line.strip() for line in g_text_rep.splitlines()]
    for line in lines:
        node = line.strip('\n')
        node = node.replace(' -> ', ' ')
        node = node.split(' ')
        adj_list.setdefault(node[0], [])
        for number in node[1].split(','):
            adj_list[node[0]].append(number)
            circuit_max += 1
    
    return adj_list, circuit_max


def FindEulerianCycle(adj_list, circuit_max):

    #Reduced adjacency list to keep track of traveled edges   
    red_adj_list = {}            
    red_adj_list = deepcopy(adj_list)            
            
    #Arbitrary starting point (if graph is directed/balanced)
    start = '0'
    curr_vrtx = '0'

    stack = []
    circuit = []    
    while len(circuit) != circuit_max:
        
        if red_adj_list[curr_vrtx] != []: #If neighbors exist
            stack.append(curr_vrtx)
            pick = randint(0,len(red_adj_list[curr_vrtx])-1)
            temp = deepcopy(curr_vrtx)
            curr_vrtx = red_adj_list[temp][pick]
            red_adj_list[temp].remove(curr_vrtx)
        
        else:
            circuit.append(curr_vrtx)
            curr_vrtx = stack[len(stack)-1]
            stack.pop()

    #Formatting
    path_array = [int(start)]
    path = start + '->'
    for vrtx in circuit[::-1]:
        path += (vrtx + '->')
        path_array.append(int(vrtx))
    #print(path.strip('->'))
    return path_array
