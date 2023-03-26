from collections import defaultdict
from typing import List
from pyllist import dllist
from DiGraph import DiGraph, Node

def source(g:DiGraph):
    for i, node in enumerate(g.m_nodes):
        if len(node.m_outgoing) == node.m_num_of_incoming + 1:
            return i
    return 0

def sink(g:DiGraph):
    for i, node in enumerate(g.m_nodes):
        if len(node.m_outgoing) + 1 == node.m_num_of_incoming:
            return i
    return 0

def has_Eulerian_path(g:DiGraph):
    exist = True
    numSources, numSinks = 0, 0
    for node in g.m_nodes:
        out, incoming = len(node.m_outgoing), node.m_num_of_incoming
        if out == incoming: # check for intermediate balanced node
            continue
        elif out == incoming + 1: # check for source node
            numSources += 1
            if numSources > 1:
                exist = False
                break
        elif out + 1 == incoming: # check for sink node
            numSinks += 1
            if numSinks > 1:
                exist = False
                break
        else:
            exist = False
            break
    return exist

def find_Eulerian_cycle(g: DiGraph) -> dllist:
    cycle = dllist()
    # BEGIN your code here:
    # Step 1: check if there exists an Eulerian cycle
    if not has_Eulerian_path(g):
        return cycle

    # Step 2: select a starting node to begin the cycle
    start_node = g.m_nodes[0]
    for node in g.m_nodes:
        if node.m_outgoing.size > 0:
            start_node = node
            break

    # Step 3: perform a DFS to find the Eulerian cycle
    stack = [start_node]
    while stack:
        current_node = stack[-1]
        if current_node.m_outgoing.size == 0:
            cycle.appendleft(current_node.m_label)
            stack.pop()
        else:
            next_node = current_node.m_outgoing.pop()
            g.m_nodes[next_node].m_num_of_incoming -= 1
            stack.append(g.m_nodes[next_node])

    # END your code above
    return cycle

def find_Eulerian_path(g:DiGraph):
    path, cycle = dllist(), dllist()

    src = source(g)
    dest = sink(g)

    #print(src, len(g.m_nodes), dest)

    src = 0 if src >= len(g.m_nodes) else src
    dest = 0 if dest >= len(g.m_nodes) else dest

    nodes = g.m_nodes
    nodes[dest].m_outgoing.append(src)
    nodes[src].m_num_of_incoming +=1
    g.m_nodes = nodes
    
    cycle = find_Eulerian_cycle(g)

    print(cycle)
    
    start_node = cycle.first.value

    print("start_node: ", start_node)
    for node in cycle:
        path.append(node)
        if node == start_node and len(path) > 1:
            break
    
    '''
    pos_dest, pos_src = dllist(), dllist()
    pos_dest = cycle.first
    while pos_dest != cycle.last:
        pos_src = pos_dest.next
        pos_dest = pos_src
        print(src, dest, g.m_nodes[src].m_label, pos_src.value, g.m_nodes[dest].m_label, pos_dest.value)
        if pos_src:
            if pos_src.value == g.m_nodes[src].m_label and pos_dest.value == g.m_nodes[dest].m_label:
                break
        else:
            break
    print("pos_src, pos_dest: ",pos_src, pos_dest)
    print(pos_src, cycle.last, pos_dest, cycle.last)
    '''
    return path