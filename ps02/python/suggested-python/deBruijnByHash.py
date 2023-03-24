from collections import defaultdict
from pyllist import dllist
from DiGraph import DiGraph, Node

class DNAHasher:
  # Hash function used for DNA sequence
  def __call__(self, seq):
    val = 0
    # TO DO: Write a DNA sequence hash function here

    # BEGIN your code here:
    
    # END your code above
    return val

class AlphabetHasher:
  # An example hash function used for the English alphabet
  def __call__(self, seq):
    val = 0
    max_width = 20
    for i in range(min(len(seq), max_width)):
      val = val << 5
      val += ord(seq[i].lower()) - ord('a')
    return val

# define the hash table class
# CSeqHash = defaultdict(list) # for unordered_multimap
CSeqHash = {}

def create_hash_table(kmers):
  # create one hash table by inserting both the prefix and suffix of each
  # k-mer. The prefix and suffix is the key. Associated with each element
  # in the hash table is the node id for that prefix or suffix in the
  # de Bruijn graph to be constructed.
  ht = {}
  node_id = 0 # the node id will be used in the de Bruijn graph
  for kmer in kmers:
    for j in range(2): # j=0: prefix; j=1: suffix
      key = kmer[j:len(kmer)-1+j]
      if key not in ht:
        ht[key] = node_id
        node_id += 1
  return ht

def create_deBruijn_graph_by_hashing(kmers):
  # create a deBruijn graph by inserting all k-mers into the graph by hashing
  
  # BEGIN your code below:
  
  # create one hash table for both the k-1 prefix and suffix of
  # each k-mer
  ht = create_hash_table(kmers)
  
  # initialize an empty node vector for graph g
  g = {}

  # for each k-mer
  for kmer in kmers:
    # find the prefix node id from_id from the hash table
    from_id = ht[kmer[:-1]]
    # update node from_id's label to prefix if necessary
    if from_id not in g:
      g[from_id] = {'label': kmer[:-1], 'outgoing': [], 'incoming': 0}
    
    # find the suffix node id to_id from the hash table
    to_id = ht[kmer[1:]]
    # update node to_id's label to suffix if necessary
    if to_id not in g:
      g[to_id] = {'label': kmer[1:], 'outgoing': [], 'incoming': 0}
    
    # create a new edge (from_id, to_id) by inserting node
    # to_id into the adjaceny list of node from_id
    g[from_id]['outgoing'].append(to_id)

    # update the number of incoming edges of node to_id
    g[to_id]['incoming'] += 1

  # end for loop
  return g
