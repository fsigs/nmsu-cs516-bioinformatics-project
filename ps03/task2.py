from task1 import hamming_distance_matrix
from Bio.Phylo.TreeConstruction import DistanceMatrix
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

def tree_by_neighbor_joining(distance_matrix):
  # Convert the distance matrix to a BioPython DistanceMatrix object
  biopython_dist_matrix = DistanceMatrix(names=sequences, matrix=distance_matrix.tolist())
  # Choose a method to construct the tree
  constructor = DistanceTreeConstructor()
  # Construct the tree using neighbor joining
  tree = constructor.nj(biopython_dist_matrix)
  # Construct the tree using neighbor joining
  tree = constructor.nj(biopython_dist_matrix)
  # Choose a root for the tree by setting the midpoint as the outgroup
  tree.root_with_outgroup({"name": "midpoint"})
  # Print the rooted tree in Newick format
  print(tree.rooted().format("newick"))

if __name__ == '__main__':
  sequences = ["ACGT", "AGTT", "ATCC", "GTCA"]
  distance_matrix = hamming_distance_matrix(sequences)
  tree_by_neighbor_joining(distance_matrix)