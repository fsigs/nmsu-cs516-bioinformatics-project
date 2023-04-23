from task2 import tree_by_neighbor_joining
import numpy as np
from Bio import Phylo

'''def small_parsimony(tree):
  nucleotides = ['A', 'C', 'G', 'T']
  for node in tree.get_nonterminals(order='postorder'):
    print(node.clades)'''

from Bio import Phylo

def small_parsimony(tree):
  # Initialize root with all possible characters
  for node in tree.get_terminals():
    seq = {c: 0 if node.name == c else float('inf') for c in 'ACGT'}
    node.seq = seq
    print(node, node.seq)
  # Bottom-up approach to fill internal nodes
  for node in tree.get_nonterminals(order='postorder'):
    left = node.clades[0]
    right = node.clades[1]
    seq = {c: float('inf') for c in 'ACGT'}
    # Compute minimum score for each character
    for c in 'ACGT':
      for c1 in left.seq:
        score = left.seq[c1] + (0 if c == c1 else 1)
        seq[c] = min(seq[c], score)
      for c2 in right.seq:
        score = right.seq[c2] + (0 if c == c2 else 1)
        seq[c] = min(seq[c], score)

    node.seq = seq
  exit()
  # Get the sequence for the root
  root_seq = {}
  for c in 'ACGT':
      score = tree.root.clades[0].seq[c] + tree.root.clades[1].seq[c]
      root_seq[c] = score
  
  tree.root.seq = root_seq
  
  # Infer the sequences for the internal nodes
  for node in tree.get_nonterminals(order='preorder'):
      left = node.clades[0]
      right = node.clades[1]
      seq = ''
      
      for i in range(len(left.seq)):
          min_score = float('inf')
          min_char = ''
          for c in 'ACGT':
              score = left.seq[c] + right.seq[c] + (0 if c == node.seq[i] else 1)
              if score < min_score:
                  min_score = score
                  min_char = c
          seq += min_char
      
      node.seq = seq
  
  # Return the tree with inferred ancestral sequences
  return tree

if __name__ == '__main__':
  sequences = ["ACGTAGGCCT", "ATGTAAGACT", "TCGAGAGCAC", "TCGAAAGCAT"]
  tree = tree_by_neighbor_joining(sequences, True, "ascii")
  small_parsimony(tree)