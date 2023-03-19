from pyllist import dllist
from DiGraph import DiGraph, Node

def create_deBruijn_graph_by_string_comp(kmers, g):
  nodes = []
  
  for kmer in kmers:
    k = len(kmer)
    # The "from" node:
    prefix = kmer[:k-1]

    # find for a node that matches the k-1 prefix
    i = 0 # i is the node id
    for node in nodes:
      if node.m_label == prefix:
        break
      i += 1
    else:
      # if the k-1 prefix does not exist as a node
      # in the graph, create a new node
      from_node = Node()
      from_node.m_label = prefix
      from_node.m_num_of_incoming = 0
      nodes.append(from_node)
      i = len(nodes) - 1
    
    from_itr = nodes[i]
    
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
      to_node = Node()
      to_node.m_label = suffix
      to_node.m_num_of_incoming = 0
      nodes.append(to_node)
      j = len(nodes) - 1
    
    to_itr = nodes[j]
    
    from_itr.m_outgoing.append(j)
    to_itr.m_num_of_incoming += 1
  
  # transfer the nodes from the list to a vector
  g.m_nodes = list(nodes)
