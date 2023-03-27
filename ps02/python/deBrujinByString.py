from typing import List
from pyllist import dllist
from DiGraph import DiGraph, Node

def create_deBruijn_graph_by_string_comp(kmers: List[str], g: DiGraph):
  nodes = dllist()

  for kmer in kmers:
    k = len(kmer)

    # The "from" node:
    prefix = kmer[0:k-1]

    # find for a node that matches the k-1 prefix
    itr = nodes.first
    i = 0  # i is the node id
    while itr is not None:
      if itr.value.m_label == prefix:
        break
      itr = itr.next
      i += 1

    if itr is None:
      # if the k-1 prefix does not exist as a node
      #   in the graph, create a new node
      from_node = Node(prefix)
      #from_node.m_label = prefix
      from_node.m_num_of_incoming = 0
      nodes.append(from_node)
      itr = nodes.last

    from_itr = itr

    # The "to" node:
    suffix = kmer[1:k]

    # find the k-1 suffix
    itr = nodes.first
    j = 0
    while itr is not None:
      if itr.value.m_label == suffix:
        break
      itr = itr.next
      j += 1

    if itr is None:
      # if the k-1 suffix does not exist as a node
      #   in the graph, create a new node
      to_node = Node(suffix)
      #to_node.m_label = suffix
      to_node.m_num_of_incoming = 0

      # insert the new node to nodes
      nodes.append(to_node)

      # remember the new node position on the list
      itr = nodes.last

    to_itr = itr

    from_itr.value.m_outgoing.append(j)
    to_itr.value.m_num_of_incoming += 1

  # transfer the nodes from the list to a vector
  g.m_nodes = [node for node in nodes]
  return g