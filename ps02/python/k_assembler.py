import os
import collections

class Node:
  """
  In Node class, outgoing is a Python linked list, 
  which can grow dynamically as edges are added to the graph.
  """
  def __init__(self, label):
    self.m_label = label # a unique node label
    # a double linked list where we can use append() and popleft() methods
    # to add or remove elements from the list outgoing in constant time
    self.m_outgoing = collections.deque() 
    self.m_num_of_incoming = 0 # the total number of incoming edges

class DiGraph: 
  """
  In DiGraph class, nodes is a Python list, 
  which can grow dynamically as nodes are added to the graph.
  """
  def __init__(self):
    self.m_nodes = [] # directed graph data structure

def assemble_kmers(kmers, method, dotfile):
  seq = ""
  g = DiGraph()

  if method == "k-mer pairwise comparison":
    create_deBruijn_graph_by_string_comp(kmers, g)
  elif method == "k-mer hashing":
    create_deBruijn_graph_by_hashing(kmers, g)
  else:
    raise Exception("ERROR: unknown methods!")

  if dotfile is not None:
    printDOTFile(g, dotfile)

  if not has_Eulerian_path(g):
    raise Exception("ERROR: Eulerian path does not exist!")
  else:
    path = find_Eulerian_path(g)
    seq = build_sequence(path, g)

  return seq

def build_sequence(path:collections.deque, g:DiGraph):
  nodes = g.m_nodes
  k = len(nodes[path.popleft()].m_label) + 1

  seq = nodes[path.popleft()].m_label[:-1]
  for i in range(1, len(path)):
    node = nodes[path[i]]
    seq += node.m_label[-1]

  return seq


def printDOTFile(g:DiGraph, file):
  with open(file, 'w') as f:
    f.write('digraph {\n')
    f.write('label="de Bruijn graph"\n')

    for node in g.m_nodes:
      for to in node.m_outgoing:
        prefix = node.m_label
        suffix = g.m_nodes[to].m_label
        f.write(f'{prefix}->{suffix} [label={prefix+suffix[-1]}];\n')

    f.write('}\n')