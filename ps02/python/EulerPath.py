
from pyllist import dllist
from DiGraph import DiGraph, Node

def source(g):
  # Find a source node from g: the node has one more
  # outgoing edge than incoming edge. When such a node
  # does not exist, a value of the total number of nodes
  # is returned.
  for i in range(len(g.m_nodes)):
    if len(g.m_nodes[i].m_outgoing) == g.m_nodes[i].m_num_of_incoming + 1:
      return i
  return len(g.m_nodes)

def sink(g):
  # Find a source node from g: the node has one more
  # outgoing edge than incoming edge. When such a node
  # does not exist, a value of the total number of nodes
  # is returned.
  for i in range(len(g.m_nodes)):
    if len(g.m_nodes[i].m_outgoing) + 1 == g.m_nodes[i].m_num_of_incoming:
      return i
  return len(g.m_nodes)

def find_Eulerian_cycle(g):
  # find an Eulerian cycle from graph g
  cycle = [] # main cycle
  
  # TO-DO: insert code to find Eulerian cycle represented
  #   as a list of node id.
  # E.g., 3 -> 2 -> 0 -> 3 -> 4 -> 1 -> 3 is a cycle on
  #   a graph with 5 nodes.
  
  # BEGIN your code here:
    
  # END your code above

  return cycle

def find_Eulerian_path(g):
  # find an Eulerian path from graph g, assuming g has such a path
  path, cycle = [], []
  
  src = source(g)  # find the source node
  dest = sink(g)   # find the sink node
  
  # In the special case graph with only cycles
  #   and no source nor sink, we choose node 0 as the
  #   start and end of the Eulerian path:
  src = 0 if src >= len(g.m_nodes) else src
  dest = 0 if dest >= len(g.m_nodes) else dest
  
  nodes = g.m_nodes
  
  # add an edge from the sink node to the source node
  nodes[dest].m_outgoing.append(src)
  
  # increase the incoming degree of the source node by one
  nodes[src].m_num_of_incoming += 1
  
  cycle = find_Eulerian_cycle(g)
  
  pos_src, pos_dest = None, None
  for i, node in enumerate(cycle):
    if i == len(cycle) - 1:
      break
    if cycle[i+1] == src and node == dest:
      pos_src = i+1
      pos_dest = i
      break
  
  if pos_src is not None and pos_dest is not None:
    
    '''
    # remove the last element on the cycle which is the same
    #   with the first element on the cycle:
    cycle.pop()
    
    # Formulate a path from the cycle such that src is
    #   the first and dest is the last on the path:
    path += cycle[pos_src:]
    path += cycle[:pos_dest+1]
    '''
    
    pos = pos_src
    while pos != pos_dest:
      path.append(cycle[pos])
      pos += 1
      if pos == len(cycle):
        pos = 1
    path.append(cycle[pos])
    
  else:
    raise Exception("Searching for Eulerian path has failed!")
  
  # return the path
  return path

def has_Eulerian_path(g):
  """
  Determine if graph g has an Eulerian path. This path could be a cycle in special cases.
  """
  exist = True
  numSources = 0
  numSinks = 0

  for node in g.m_nodes:
    out = len(node.m_outgoing)
    incoming = node.m_num_of_incoming
    if out == incoming:  # Check for intermediate balanced node
      continue
    elif out == incoming + 1:  # Check for source node
      numSources += 1
      if numSources > 1:
        exist = False
        break
    elif out + 1 == incoming:  # Check for sink node
      numSinks += 1
      if numSinks > 1:
        exist = False
        break
    else:
      exist = False
      break

  return exist

