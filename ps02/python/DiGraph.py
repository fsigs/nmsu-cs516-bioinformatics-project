from pyllist import dllist

class Node:
  
  def __init__(self, label: str):
    self.m_label = label
    self.m_outgoing = dllist()
    self.m_num_of_incoming = 0

  def print(self):
    print("  ",self.m_label)
    print("   incoming: ",str(self.m_num_of_incoming))
    print("     edges: ",self.m_outgoing)
    
class DiGraph:

  def __init__(self):
    self.m_nodes = []

  def print(self):
    print("---------------------------------------")
    print(" DiGraph ", len(self.m_nodes), " nodes")
    for node in self.m_nodes:
      node.print()
    print("---------------------------------------")

  def textRepresentation(self, hide_labels = True):
    answer = ""
    for i in range(0, len(self.m_nodes)):
      node = self.m_nodes[i]
      if hide_labels:
        answer += str(i) + ' -> '
      else:
        answer += str(i) + '(' + node.m_label + ')' + ' -> '
      elems = list(node.m_outgoing)
      edges = []
      for elem in elems:
        if elem is not None:
          edges.append(str(elem))
      answer += ','.join(edges)
      answer += '\n'
    return answer

