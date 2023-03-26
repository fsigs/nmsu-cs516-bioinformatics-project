from typing import List
from pyllist import dllist
from DiGraph import DiGraph, Node

def get_len_and_label(nodes, element):
    size = 0
    label = None
    for i in range(0, len(nodes)):
        if nodes[i].m_label == element.value:
            size = len(nodes[i].m_label)
            label = nodes[i].m_label
    return size, label

def build_sequence(path: dllist, g: DiGraph) -> str:
    
    nodes = g.m_nodes
    size_first, label_first = get_len_and_label(nodes, path.first)
    print(size_first, label_first)
    k = size_first + 1
    seq = ''
    seq += label_first
    print(k,seq)
    
    pos = path.first.next
    i = k - 1
    
    while pos != path.last:
        m_size, m_label = get_len_and_label(nodes, pos)
        #seq += nodes[pos.value].m_label[-1]
        seq += m_label[-1]
        i += 1
        pos = pos.next
    print(seq) 
    return seq
    