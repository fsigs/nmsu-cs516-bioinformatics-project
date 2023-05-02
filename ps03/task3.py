import numpy as np
from timeit import default_timer as timer
from task2 import tree_by_neighbor_joining

nucleotides = 'ACGT'

def small_parsimony(tree):
  start = timer()
  sequences = [node.name for node in tree.get_terminals()]
  
  # (i-th) letter of each sequence
  words = []
  for i in range(0, len(sequences[0])):
    word = ''
    for sequence in sequences:
      word += str(sequence[i])
    words.append(word)
  
  ancestral_sequence = ''
  for word in words:
    ancestral_sequence += sp(word)
  end = timer()
  ancestral_sequence_time = end - start
  return ancestral_sequence, ancestral_sequence_time

def sp(word):
  left, right = [], []
  for i, c in enumerate(word):
    if i % 2 == 0:
      left.append(c)
    else:
      right.append(c)
  
  aditional = False
  if len(right) % 2 != 0:
    aditional = True
  
  scores_boths = []  
  for i, c in enumerate(left):
    c_left = c
    if i == len(left) - 1 and aditional == True:
      c_right = None
    else:
      c_right = right[i]
    scores_left = [0 if c_left == n else float('inf') for n in nucleotides]
    if c_right != None:
      scores_right = [0 if c_right == n else float('inf') for n in nucleotides]
    else:
      scores_right = [float('inf') for n in nucleotides]
    scores_both = scores(scores_left, scores_right)
    scores_boths.append(scores_both)

  while len(scores_boths) > 1:
    num_pairs = len(scores_boths) // 2
    pairs = []
    for i in range(num_pairs):
      start_index = i * 2
      end_index = start_index + 2
      pair = scores_boths[start_index:end_index]
      pairs.append(pair)
    scoresb = []
    for pair in pairs:
      scoresb.append(scores(pair[0], pair[1]))
    scores_boths = scoresb

  scores_boths = np.array(scores_boths).flatten()

  nucleotide_letter = None
  for i, s in enumerate(scores_boths):
    if s == min(scores_boths):
      nucleotide_letter = nucleotides[i]
  return nucleotide_letter

def scores(scores_node_left, scores_node_right):
  scores_internal_node = []
  for ni, n in enumerate(nucleotides):
    ss_left = []
    for si,s in enumerate(scores_node_left):
      ss = s + (0 if si == ni else 1)
      ss_left.append(ss)
    ss_right = []
    for si,s in enumerate(scores_node_right):
      ss = s + (0 if si == ni else 1)
      ss_right.append(ss)
    score = min(ss_left) + min(ss_right)
    scores_internal_node.append(score)
  return scores_internal_node     

if __name__ == '__main__':
  print()
  sequences = ["ACGTAGGCCT", "ATGTAAGACT", "TCGAGAGCAC", "TCGAAAGCAT"]
  tree = tree_by_neighbor_joining(sequences, True, "ascii")
  ancestral_sequence, ancestral_sequence_time = small_parsimony(tree[0])
  print("Ancestral Sequence (Small Parsimony): ",ancestral_sequence,"\n")
  print('Runing time: {:.5f} seconds'.format(ancestral_sequence_time))
  print()