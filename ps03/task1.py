import numpy as np

def hamming_distance(s1, s2):
  if len(s1) != len(s2):
    return None
  else:
    distance = 0
    for i in range(len(s1)):
      if s1[i] != s2[i]:
        distance += 1
    return distance

def triangular_inferior_format(matrix):
  triangular_matrix = []
  for i in range(len(matrix)):
    row = []
    for j in range(len(matrix)):
      if i >= j:
        row.append(matrix[i][j])
    triangular_matrix.append(row)
  return triangular_matrix

def hamming_distance_matrix(sequences, triangular=True, print_matrix=False):
  num_seqs = len(sequences)
  distance_matrix = np.zeros((num_seqs, num_seqs), dtype=int)
  
  for i in range(num_seqs):
    for j in range(num_seqs):
      if i != j:
        distance_matrix[i][j] = hamming_distance(sequences[i], sequences[j])
  
  distance_matrix_triangular = triangular_inferior_format(distance_matrix.tolist())
  
  if print_matrix == True and triangular == False:
    print(distance_matrix)
  if print_matrix == True and triangular == True:
    print(distance_matrix_triangular)

  if triangular == True:
    return distance_matrix_triangular
  else:
    return distance_matrix

if __name__ == '__main__':
  print()

  sequences = ["ACGTAGGCCT", "ATGTAAGACT", "TCGAGAGCAC", "TCGAAAGCAT"]
  print("Hamming distance matrix for sequences (normal format):\n",sequences)
  hamming_distance_matrix(sequences, False, True)
  print()

  sequences = ["ACGT", "AGTT", "ATCC", "GTCA"]
  print("Hamming distance matrix for sequences (inf. triangular format):\n",sequences)
  hamming_distance_matrix(sequences, True, True)
  print()