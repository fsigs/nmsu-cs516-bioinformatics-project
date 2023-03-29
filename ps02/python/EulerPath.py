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
    cycle_labels, cycle_values = dllist(), dllist()
    adj_list, circuit_max = CreateAdjacencyList2(g.textRepresentation())
    path = FindEulerianCycle(adj_list, circuit_max)
    for index in path:
      cycle_labels.append(g.m_nodes[index].m_label)
      cycle_values.append(index)
    return cycle_labels, cycle_values


def find_Eulerian_path(g: DiGraph) -> dllist:
  path, cycle = dllist(), dllist()
  
  src = source(g)
  dest = sink(g)
  src = 0 if src >= len(g.m_nodes) else src
  dest = 0 if dest >= len(g.m_nodes) else dest

  nodes = g.m_nodes
  nodes[dest].m_outgoing.append(src)
  nodes[src].m_num_of_incoming += 1
  g.m_nodes = nodes

  cycle_labels, cycle = find_Eulerian_cycle(g) 
  cycle.pop()
  cycle_labels.pop()
  
  src_times = 0
  for id in cycle:
    if id == src:
      src_times += 1
 
  first_part = []
  count = 1
  cur_first_part = cycle.first
  while cur_first_part.next is not None:
    if count == src_times and cur_first_part.value == src:
      break
    if cur_first_part.value == src:
      count += 1
    first_part.append(cur_first_part.value)
    cur_first_part = cur_first_part.next

  cur_last_part = cycle.last
  last_part = []
  while cur_last_part.value != src:
    last_part.append(cur_last_part.value)
    cur_last_part = cur_last_part.prev
  
  path_ids = [src] 
  if last_part is not None:
    path_ids += last_part[::-1]
  if first_part is not None:
    path_ids += first_part
  
  path = dllist()
  if len(path_ids) > 0:
    for id in path_ids:
      path.append(g.m_nodes[id].m_label)
  else:
    path.append(src)

  return path