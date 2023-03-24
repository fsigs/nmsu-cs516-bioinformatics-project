from pyllist import dllist

class Node:
  """
  In Node class, m_outgoing is a Python linked list using pllist, 
  which can grow dynamically as edges are added to the graph.
  """
  def __init__(self, label):
    self.m_label = label # a unique node label
    self.m_outgoing = dllist()
    self.m_num_of_incoming = 0 # the total number of incoming edges

class DiGraph: 
  """
  In DiGraph class, nodes is a Python list, 
  which can grow dynamically as nodes are added to the graph.
  """
  def __init__(self):
    self.m_nodes = [] # directed graph data structure