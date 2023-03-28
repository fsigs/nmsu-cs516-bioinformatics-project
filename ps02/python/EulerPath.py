from collections import defaultdict
from typing import List
from pyllist import dllist
from DiGraph import DiGraph, Node
from random import choice
from EulerianCycle import CreateAdjacencyList2, FindEulerianCycle

def source(g:DiGraph):
  for i, node in enumerate(g.m_nodes):
    if len(node.m_outgoing) == node.m_num_of_incoming + 1:
      return i
  return 0

def sink(g:DiGraph):
  for i, node in enumerate(g.m_nodes):
    if len(node.m_outgoing) + 1 == node.m_num_of_incoming:
      return i
  return 0

def has_Eulerian_path(g:DiGraph):
  exist = True
  numSources, numSinks = 0, 0
  for node in g.m_nodes:
    out, incoming = len(node.m_outgoing), node.m_num_of_incoming
    if out == incoming: # check for intermediate balanced node
      continue
    elif out == incoming + 1: # check for source node
      numSources += 1
      if numSources > 1:
        exist = False
        break
    elif out + 1 == incoming: # check for sink node
      numSinks += 1
      if numSinks > 1:
        exist = False
        break
    else:
      exist = False
      break
  return exist

def find_Eulerian_cycle(g: DiGraph) -> dllist:
    cycle = dllist()
    adj_list, circuit_max = CreateAdjacencyList2(g.textRepresentation())
    path = FindEulerianCycle(adj_list, circuit_max)
    for index in path:
      cycle.append(g.m_nodes[index].m_label)
    return cycle


def find_Eulerian_path(g: DiGraph) -> dllist:
  path = dllist()
  cycle = dllist()

  src = source(g)
  dest = sink(g)

  #print("src,dest: ",(src,dest))

  # In the special case graph with only cycles
  # and no source nor sink, we choose node 0 as the
  # start and end of the Eulerian path:
  src = 0 if src >= len(g.m_nodes) else src
  dest = 0 if dest >= len(g.m_nodes) else dest

  nodes = g.m_nodes

  # add an edge from the sink node to the source node
  nodes[dest].m_outgoing.append(src)

  # increase the incoming degree of the source node by one
  nodes[src].m_num_of_incoming += 1

  g.m_nodes = nodes 
  
  #g.print()
  
  cycle = find_Eulerian_cycle(g)
  
  #print("Eulerian_cycle: ", cycle)
  
  pos_dest = cycle.first
  pos_src = pos_dest.next

  while pos_src:
    if pos_src.next:
      if pos_src.value == src and pos_dest.value == dest:
        break
    else:
      break
    pos_dest = pos_src
    pos_src = pos_src.next

  if pos_src and pos_dest:
    pos = pos_src
    while True:
      path.append(pos.value)
      pos = pos.next
      if not pos:
        pos = cycle.first.next
      if pos == pos_src:
        break
  else:
    raise Exception("Searching for Eulerian path has failed!")

  return path