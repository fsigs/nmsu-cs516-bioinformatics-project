import os
from pyllist import dllist
from DiGraph import DiGraph, Node

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

def build_sequence(path:dllist, g:DiGraph):
  nodes = g.m_nodes
  k = len(nodes[path.first].m_label) + 1

  seq = nodes[path.first].m_label[:-1]
  for i in range(1, len(path)):
    node = nodes[path.nodeat(i)]
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