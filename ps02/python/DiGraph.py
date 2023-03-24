from pyllist import dllist

class Node:
  def __init__(self, label: str):
    self.m_label = label
    self.m_outgoing = dllist()
    self.m_num_of_incoming = 0

class DiGraph:
  def __init__(self):
    self.m_nodes = []