# FrequentKmers.py
import numpy as np
from timeit import default_timer as timer

class FrequentKmers:

  def __init__(self, word=""):
    self.word = word
  
  def frequent_words(self, text, k):
    start = timer()
    frequent_words = []
    
    #your code here
    
    end = timer()
    return [frequent_words,  round((end - start) * 1000, 3)]
  
  #see slide ch1 96
  def better_frequent_words(self, text, k):
    start = timer()
    freq_map = self.frequent_map(text, k)
    max_count = max(freq_map.values())
    frequent_words = []
    for pattern in freq_map.items():
      if pattern[1] == max_count:
        frequent_words.append(pattern[0])
    end = timer()
    return [frequent_words,  round((end - start) * 1000, 3)]
  
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
  
  def read_covid_txt_file(self):
    None