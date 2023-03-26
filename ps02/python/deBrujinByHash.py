from collections import defaultdict
from typing import List
from pyllist import dllist
from DiGraph import DiGraph, Node

class DNAHasher:
  def __call__(self, seq: str) -> int:
    val = 0
    max_width = 20
    for i in range(min(len(seq), max_width)):
      val = val << 2
      # A=00, C=01, G=10, and T=11
      c = seq[i].lower()
      if c == 'a':
        val += 0
      elif c == 'c':
        val += 1
      elif c == 'g':
        val += 2
      elif c == 't':
        val += 3
      else:
        raise ValueError(f"Invalid base at position {i}: {seq[i]}")
    return val

class CSeqHash:
    def __init__(self):
        self.ht = defaultdict(dllist)

    def insert(self, key, value):
        self.ht[key].appendright(value)

    def find(self, key):
        return self.ht.get(key, None)

def create_hash_table(kmers: List[str]) -> CSeqHash:
    ht = CSeqHash()
    node_id = 0  # the node id will be used in the de Bruijn graph
    for kmer in kmers:
        for j in range(2):  # j=0: prefix; j=1: suffix
            key = kmer[j:len(kmer)-1]
            if not ht.find(key):
                ht.insert(key, node_id)
                node_id += 1
    return ht

def create_deBruijn_graph_by_hashing(kmers: List[str], g: DiGraph):
    # create one hash table for both the k-1 prefix and suffix of each k-mer
    seq_hash = CSeqHash()

    # initialize an empty node vector for graph g
    node_id = {}

    # for each k-mer
    for kmer in kmers:
        kmer_len = len(kmer)
        prefix = kmer[0:kmer_len-1]
        suffix = kmer[1:kmer_len]

        # hash the prefix and suffix strings to get unique integer ids
        prefix_id = DNAHasher()(prefix)
        suffix_id = DNAHasher()(suffix)

        # find the prefix node id from the hash table
        if prefix_id in node_id:
            from_id = node_id[prefix_id]
        else:
            # create a new node and add it to the graph and node_id dict
            from_node = Node(prefix)
            g.m_nodes.append(from_node)
            node_id[prefix_id] = len(g.m_nodes) - 1
            from_id = node_id[prefix_id]
            # insert the new node into the hash table
            seq_hash.insert(prefix_id, from_id)

        # update node from_id's label to prefix if necessary
        if g.m_nodes[from_id].m_label != prefix:
            g.m_nodes[from_id].m_label = prefix

        # find the suffix node id to_id from the hash table
        if suffix_id in node_id:
            to_id = node_id[suffix_id]
        else:
            # create a new node and add it to the graph and node_id dict
            to_node = Node(suffix)
            g.m_nodes.append(to_node)
            node_id[suffix_id] = len(g.m_nodes) - 1
            to_id = node_id[suffix_id]
            # insert the new node into the hash table
            seq_hash.insert(suffix_id, to_id)

        # update node to_id's label to suffix if necessary
        if g.m_nodes[to_id].m_label != suffix:
            g.m_nodes[to_id].m_label = suffix

        # create a new edge (from_id, to_id) by inserting node to_id into the adjaceny list of node from_id
        g.m_nodes[from_id].m_outgoing.appendright(to_id)

        # update the number of incoming edges of node to_id
        g.m_nodes[to_id].m_num_of_incoming += 1
    
    # end for loop
    return g