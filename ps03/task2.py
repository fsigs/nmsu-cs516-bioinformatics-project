from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceMatrix
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from task1 import hamming_distance_matrix, get_sequences_from_fasta_file
from timeit import default_timer as timer

def tree_by_neighbor_joining(sequences, plot = False, plot_type='ascii'):
  start = timer()
  distance_matrix, distance_matrix_time = hamming_distance_matrix(sequences)
  biopython_dist_matrix = DistanceMatrix(names=sequences, matrix=distance_matrix)
  constructor = DistanceTreeConstructor()
  tree = constructor.nj(biopython_dist_matrix)
  midpoint_clade = list(tree.find_clades(name="midpoint"))
  tree.root_with_outgroup(midpoint_clade)
  end = timer()
  tree_generation_time = end - start
  if plot and plot_type == 'ascii':
    Phylo.draw_ascii(tree)
  if plot and plot_type == 'image':
    Phylo.draw(tree)
  return tree, tree_generation_time

if __name__ == '__main__':
  print()
  #sequences = ["ACGTAGGCCT", "ATGTAAGACT", "TCGAGAGCAC", "TCGAAAGCAT"]
  sequences = get_sequences_from_fasta_file('./fasta-sequences/fasta2.txt')
  print("Rooted phylogenetic tree (Neighbor Joining) for sequences:\n\n",sequences,"\n")
  tree, tree_generation_time = tree_by_neighbor_joining(sequences, True, "ascii")
  print('Runing time: {:.5f} seconds'.format(tree_generation_time))
  print()