from DiGraph import DiGraph

def source(g):
    for i, node in enumerate(g.m_nodes):
        if len(node.m_outgoing) == node.m_num_of_incoming + 1:
            return i
    return None

def sink(g):
    for i, node in enumerate(g.m_nodes):
        if len(node.m_outgoing) + 1 == node.m_num_of_incoming:
            return i
    return None

def has_Eulerian_path(g):
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
