from task1 import hamming_distance_matrix
from Bio.Phylo.TreeConstruction import DistanceMatrix
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import Phylo

def tree_by_neighbor_joining(sequences, plot = False, plot_type='ascii'):
  distance_matrix = hamming_distance_matrix(sequences)
  biopython_dist_matrix = DistanceMatrix(names=sequences, matrix=distance_matrix)
  constructor = DistanceTreeConstructor()
  tree = constructor.nj(biopython_dist_matrix)
  midpoint_clade = list(tree.find_clades(name="midpoint"))
  tree.root_with_outgroup(midpoint_clade)
  if plot and plot_type == 'ascii':
    Phylo.draw_ascii(tree)
  if plot and plot_type == 'image':
    Phylo.draw(tree)
  return tree

if __name__ == '__main__':
  sequences = ["ACGTAGGCCT", "ATGTAAGACT", "TCGAGAGCAC", "TCGAAAGCAT"]
  tree_by_neighbor_joining(sequences)