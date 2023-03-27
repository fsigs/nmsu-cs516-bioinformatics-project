def find_Eulerian_cycle(g: DiGraph) -> dllist:
  cycle = dllist()
  # BEGIN your code here:
  # Step 1: check if there exists an Eulerian cycle
  if not has_Eulerian_path(g):
    return cycle

  # Step 2: select a starting node to begin the cycle
  start_node = g.m_nodes[0]
  for node in g.m_nodes:
    if node.m_outgoing.size > 0:
      start_node = node
      break

  # Step 3: perform a DFS to find the Eulerian cycle
  stack = [start_node]
  while stack:
    current_node = stack[-1]
    if current_node.m_outgoing.size == 0:
      cycle.appendleft(current_node.m_label)
      stack.pop()
    else:
      next_node = current_node.m_outgoing.pop()
      g.m_nodes[next_node].m_num_of_incoming -= 1
      stack.append(g.m_nodes[next_node])

  # END your code above
  return cycle