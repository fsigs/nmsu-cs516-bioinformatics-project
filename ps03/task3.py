from task2 import tree_by_neighbor_joining
import numpy as np
from Bio import Phylo

def small_parsimony(tree):
  nucleotides = ['A', 'C', 'G', 'T']
  for node in tree.get_nonterminals(order='postorder'):
    print(node.clades)

if __name__ == '__main__':
  sequences = ["ACGTAGGCCT", "ATGTAAGACT", "TCGAGAGCAC", "TCGAAAGCAT"]
  tree = tree_by_neighbor_joining(sequences)
  small_parsimony(tree)