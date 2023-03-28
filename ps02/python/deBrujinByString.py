from typing import List
from pyllist import dllist
from DiGraph import DiGraph, Node

def create_deBruijn_graph_by_string_comp(kmers: List[str], g: DiGraph):
  
  nodes = dllist()

  for kmer in kmers:
    k = len(kmer)

    prefix = kmer[0:k-1]

    itr = nodes.first
    i = 0
    while itr is not None:
      if itr.value.m_label == prefix:
        break
      itr = itr.next
      i += 1

    if itr is None:
      from_node = Node(prefix)
      from_node.m_num_of_incoming = 0
      nodes.append(from_node)
      itr = nodes.last

    from_itr = itr

    suffix = kmer[1:k]

    itr = nodes.first
    j = 0
    while itr is not None:
      if itr.value.m_label == suffix:
        break
      itr = itr.next
      j += 1

    if itr is None:
      to_node = Node(suffix)
      to_node.m_num_of_incoming = 0

      nodes.append(to_node)

      itr = nodes.last

    to_itr = itr

    from_itr.value.m_outgoing.append(j)
    to_itr.value.m_num_of_incoming += 1

  g.m_nodes = [node for node in nodes]
  return g
