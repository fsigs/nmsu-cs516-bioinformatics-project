from typing import List
from pyllist import dllist
from DiGraph import DiGraph, Node
from deBrujinByString import create_deBruijn_graph_by_string_comp
from deBrujinByHash import create_deBruijn_graph_by_hashing
from EulerPath import has_Eulerian_path, find_Eulerian_path

def dllist_index(my_list, elem):
    index = 0
    current_node = my_list.first
    while current_node is not None:
        if current_node.value == elem:
            break
        current_node = current_node.next
        index += 1
    return index

def build_sequence(path: dllist, g: DiGraph) -> str:
    k = len(path.first.value) + 1
    seq = path.first.value[:k-1]
    pos = path.first.next
    while pos != path.last:
        seq += pos.value[-1]
        pos = pos.next
    seq += path.last.value[-1]
    return seq

def assemble_kmers(kmers, method, dotfile=None):
    seq = ""
    g = DiGraph()
    if method == "k-mer pairwise comparison":
        create_deBruijn_graph_by_string_comp(kmers, g)
    elif method == "k-mer hashing":
        create_deBruijn_graph_by_hashing(kmers, g)
    else:
        raise ValueError("ERROR: unknown methods!")
    if dotfile:
        printDOTFile(g, dotfile)
    if not has_Eulerian_path(g):
        raise ValueError("ERROR: Eulerian path does not exist!")
    else:
        path = find_Eulerian_path(g)
        seq = build_sequence(path, g)
    return seq

def printDOTFile(g, file):
    with open(file, 'w') as ofs:
        ofs.write("digraph {\n")
        ofs.write("label=\"de Bruijn graph\"\n")
        nodes = g.m_nodes
        for node in nodes:
            for to in node.m_outgoing:
                prefix = node.m_label
                suffix = nodes[to].m_label
                ofs.write(f"{prefix}->{suffix}[label={prefix}{suffix[-1]}];\n")
        ofs.write("}\n")