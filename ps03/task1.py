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

def hamming_distance_matrix(sequences):
  num_seqs = len(sequences)
  distance_matrix = np.zeros((num_seqs, num_seqs))
  for i in range(num_seqs):
    for j in range(num_seqs):
      if i != j:
        distance_matrix[i][j] = hamming_distance(sequences[i], sequences[j])
  return distance_matrix

if __name__ == '__main__':
  sequences = ["ACGT", "AGTT", "ATCC", "GTCA"]
  print(hamming_distance_matrix(sequences))