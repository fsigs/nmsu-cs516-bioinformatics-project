import random
from k_assembler import assemble_kmers
from k_assembler import build_sequence

def random_DNA_sequence(min_length=10, max_length=10000):
  # generate a DNA sequence of length in the given range
  length = random.randint(min_length, max_length)
  
  # random generate the DNA sequence using alphabet atgc
  nucleotides = "atgc"
  DNA = ''.join(random.choices(nucleotides, k=length))
  
  return DNA

def get_kmers(seq, k, randomized=True):
  # obtain all k-mers of a given sequence. The order of the k-mers
  # is randomized by default.
  kmers = [seq[i:i+k] for i in range(len(seq) - k + 1)]
  
  if randomized:
    # shuffle the order of the kmers
    random.shuffle(kmers)
  
  return kmers

def compare_composition(s1, s2, k):
  # compare the canonical composition of two sequences. Canonical
  # composition is all k-mers arranged in dictionary order.
  same_composition = True
  
  if len(s1) != len(s2):
    same_composition = False
  elif s1 == s2:
    same_composition = True
  else:
    composition1 = get_kmers(s1, k)
    composition1.sort()
    composition2 = get_kmers(s2, k)
    composition2.sort()
    same_composition = composition1 == composition2
  
  return same_composition
