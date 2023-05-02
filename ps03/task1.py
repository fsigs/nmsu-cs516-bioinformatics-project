import numpy as np
from timeit import default_timer as timer

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

def get_sequences_from_fasta_file(file_path):
  sequences = []
  line_sequence = 1
  file = open(file_path, 'r')
  for line in file:
    if line_sequence%2 == 0:
      sequences.append(line.replace('\n', ''))
    line_sequence += 1
  file.close()
  return sequences

def hamming_distance_matrix(sequences, triangular=True, print_matrix=False):
  num_seqs = len(sequences)
  distance_matrix = np.zeros((num_seqs, num_seqs), dtype=int)
 
  start = timer()
  for i in range(num_seqs):
    for j in range(num_seqs):
      if i != j:
        distance_matrix[i][j] = hamming_distance(sequences[i], sequences[j])
  end = timer()
  hamming_distance_matrix_time = end - start

  distance_matrix_triangular = triangular_inferior_format(distance_matrix.tolist())
  
  if print_matrix == True and triangular == False:
    print(distance_matrix)
  if print_matrix == True and triangular == True:
    print(distance_matrix_triangular)

  if triangular == True:
    return distance_matrix_triangular, hamming_distance_matrix_time
  else:
    return distance_matrix, hamming_distance_matrix_time
  

if __name__ == '__main__':
  print()
  print("\nSequences from array")
  print("====================")

  # Directly specifying arrays and getting a normal squared matrix
  sequences = ["ACGTAGGCCT", "ATGTAAGACT", "TCGAGAGCAC", "TCGAAAGCAT"]
  print("Hamming distance matrix for sequences (normal format):\n",sequences,"\n")
  m, t = hamming_distance_matrix(sequences, False, True)
  print('\n  Runing time: {:.5f} seconds'.format(t))
  print()

  # Directly specifying arrays and getting an inferior triangular matrix as BioPython uses
  sequences = ["ACGT", "AGTT", "ATCC", "GTCA"]
  print("Hamming distance matrix for sequences (inf. triangular format):\n",sequences,"\n")
  m, t = hamming_distance_matrix(sequences, True, True)
  print('\n  Runing time: {:.5f} seconds'.format(t))
  print()

  print("\nSequences from Fasta files")
  print("==========================")

  # From fasta file, reads virus kmers and produces a normal squared matrix
  sequences = get_sequences_from_fasta_file('./fasta-sequences/fasta2.txt')
  print("Hamming distance matrix for sequences (normal format):\n",sequences,"\n")
  m, t = hamming_distance_matrix(sequences, False, True)
  print('\n  Runing time: {:.5f} seconds'.format(t))
  print()

  # From fasta file, reads virus kmers and produces an inferior triangular matrix as BioPython uses
  sequences = get_sequences_from_fasta_file('./fasta-sequences/fasta2.txt')
  print("Hamming distance matrix for sequences (inf. triangular format):\n",sequences,"\n")
  m, t = hamming_distance_matrix(sequences, True, True)
  print('\n  Runing time: {:.5f} seconds'.format(t))
  print()
