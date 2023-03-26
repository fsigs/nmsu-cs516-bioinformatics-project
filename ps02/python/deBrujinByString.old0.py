from typing import List
from pyllist import dllist
from DiGraph import DiGraph, Node

def create_deBruijn_graph_by_string_comp(kmers: List[str], g: DiGraph):
  nodes = dllist()

  for kmer in kmers:
    k = len(kmer)
    # The "from" node:
    prefix = kmer[:k-1]
    # find for a node that matches the k-1 prefix
    i = 0  # i is the node id
    for node in nodes:
      if node.m_label == prefix:
        break
      i += 1
    else:
      # if the k-1 prefix does not exist as a node
      # in the graph, create a new node
      from_node = Node(prefix)
      from_node.m_num_of_incoming = 0
      nodes.append(from_node)
      node_iter = nodes.last

    from_iter = node_iter
    # The "to" node:
    suffix = kmer[1:]
    # find the k-1 suffix
    j = 0
    for node in nodes:
      if node.m_label == suffix:
        break
      j += 1
    else:
      # if the k-1 suffix does not exist as a node
      # in the graph, create a new node
      to_node = Node(suffix)
      to_node.m_num_of_incoming = 0

      # insert the new node to nodes
      nodes.append(to_node)

      # remember the new node position on the list
      node_iter = nodes.last

    to_iter = node_iter

    from_iter.value.m_outgoing.append(j)
    to_iter.value.m_num_of_incoming += 1

  # transfer the nodes from the list to a vector
  g.m_nodes = [node for node in nodes]

  return g
