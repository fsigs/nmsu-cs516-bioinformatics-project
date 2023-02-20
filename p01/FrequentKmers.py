# FrequentKmers.py
import numpy as np

class FrequentKmers:

  def __init__(self, word=""):
    self.word = word
  
  def frequent_words(self, text, k):
    return None
  
  #see slide ch1 96
  def better_frequent_words(self, text, k):
    freq_map = self.frequent_map(text, k)
    max_count = max(freq_map.values())
    answer = []
    for pattern in freq_map.items():
      if pattern[1] == max_count:
        answer.append(pattern[0])
    return answer
  
  def frequent_map(self, text, k):
    freq_map = {}
    n = len(text)
    for i in range(n - k + 1):
      pattern = text[i:i+k]
      if pattern is not None:
        if pattern in freq_map:
          freq_map[pattern] += 1
        else:
          freq_map[pattern] = 1
    return freq_map

  def generate_dna(self, L):
    sequence = np.random.choice(['A', 'C', 'G', 'T'], size=L, p=[0.25, 0.25, 0.25, 0.25])
    return ''.join(sequence)