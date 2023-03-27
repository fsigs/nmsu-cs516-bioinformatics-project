import random

def random_DNA_sequence(min_length=10, max_length=100):#min_length=10, max_length=10000
  length = random.randint(min_length, max_length)
  DNA = ''.join(random.choice('atgc') for _ in range(length))
  return DNA

def get_kmers(seq, k, randomized=True):
  kmers = [seq[i:i+k] for i in range(len(seq) - k + 1)]
  if randomized:
    randomized_kmers = list(kmers)
    nkmers = len(kmers)
    for i in range(nkmers - 1):
      j = random.randint(i, nkmers - 1)
      randomized_kmers[i], randomized_kmers[j] = randomized_kmers[j], randomized_kmers[i]
    return randomized_kmers
  else:
    return kmers

def compare_composition(s1: str, s2: str, k: int) -> bool:
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