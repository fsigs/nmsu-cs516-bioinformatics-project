# FrequentKmers.py
import numpy as np

class FrequentKmers:

  def __init__(self, word=""):
    self.word = word
  
  def count_by_counting(self):
    return None
  
  #see slide ch1 96
  def better_frequent_words(self, text, k):
    freq_map = self.frequent_map(text, k)
    max_count = max(freq_map.values())
    for pattern in freq_map:
      print(pattern)
    return None
  
  def frequent_map(self, text, k):
    freq_map = {}
    n = len(text)
    for i in range(n - k + 1):
      pattern = text[i:i+k]
      if pattern in freq_map:
        freq_map[pattern] += 1
      else:
        freq_map[pattern] = 1
    return freq_map

  def generate_dna(self, L):
    nucleotides = ['A', 'C', 'G', 'T']
    probabilities = [0.25, 0.25, 0.25, 0.25]
    sequence = np.random.choice(nucleotides, size=L, p=probabilities)
    return ''.join(sequence)