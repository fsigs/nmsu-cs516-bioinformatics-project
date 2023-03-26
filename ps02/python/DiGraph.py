from pyllist import dllist

class Node:
  def __init__(self, label: str):
    self.m_label = label
    self.m_outgoing = dllist()
    self.m_num_of_incoming = 0
  def print(self, nodes):
    print(" Node: ", self.m_label, " (incoming: ", self.m_num_of_incoming, ", outcoming:", len(self.m_outgoing),")")
    for node in self.m_outgoing:
      print("  ", node)

class DiGraph:
  def __init__(self):
    self.m_nodes = []
  def print(self):
    print("* DiGraph: ", len(self.m_nodes))
    for node in self.m_nodes:
      node.print(self.m_nodes)