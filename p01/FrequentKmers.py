# FrequentKmers.py Class
import re
import numpy as np
import random
from timeit import default_timer as timer

class FrequentKmers:

  def __init__(self, word=""):
    self.word = word
  
  # Frequent Words Algorithm methods:
  def frequent_words(self, text, k):
    start = timer()
    frequent_words = []
    n = len(text)
    count_array = np.zeros(n - k + 1)
    for i in range(n - k + 1):
      pattern = text[i:i+k]
      count_array[i] = self.pattern_count(text, pattern)
    for i in self.max_array(count_array):
      frequent_words.append(text[i:i+k])
    frequent_words = self.remove_duplicates(frequent_words)
    end = timer()
    return [frequent_words,  round((end - start) * 1000, 3)]
  
  def pattern_count(self, text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
      if text[i:i+len(pattern)] == pattern:
        count += 1
    return count
  
  def remove_duplicates(self, arr):
    answer = []
    for item in arr:
      if item not in answer:
        answer.append(item)
    return answer

  def max_array(self, arr):
    max_val = max(arr)
    max_indices = [i for i, val in enumerate(arr) if val == max_val]
    return max_indices

  # Better Frequent Words Algorithm methods:
  def better_frequent_words(self, text, k):
    start = timer()
    freq_map = self.frequent_map(text, k)
    if freq_map is not None:
      max_count = max(freq_map.values())
      frequent_words = []
      for pattern in freq_map.items():
        if pattern[1] == max_count:
          frequent_words.append(pattern[0])
      end = timer()
      return [frequent_words, round((end - start) * 1000, 3)]
    else:
      end = timer()
      return[None, round((end - start) * 1000, 3)]
  
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

  # Random DNA generator method:
  def generate_dna(self, L):
    return ''.join(np.random.choice(['A', 'C', 'G', 'T'], size=L, p=[0.25, 0.25, 0.25, 0.25]))
  
  # Remover of polyA tail
  def remove_polyA(self, sequence, tail_length):
    pattern = "A{" + str(tail_length) + ",}$"
    match = re.search(pattern, sequence)
    if match:
      sequence = sequence[:(match.start())]
    return sequence
  
  # Reader of Covid genome files:
  def get_covid_genome(self, filename):
    with open(filename, 'r') as file:
      sequence = file.read().replace('\n', '').strip()
    tail_length = 10
    if(filename == "SARS-CoV-2.txt"):
      tail_length = 33
    if(filename == "SARS-CoV.txt"):
      tail_length = 24
    return self.remove_polyA(sequence, tail_length)

  # Permutation test (null distribution):
  def permutation_test(self, text, k, num_perm):
    p_value = None
    fm = self.frequent_map(text, k)
    max_count = max(fm.values())
    null_population = list(text)
    null_distribution = []
    for _ in range(num_perm):
      random.shuffle(null_population)
      fm2 = self.frequent_map(''.join(null_population), k)
      null_counts = max(fm2.values())
      null_distribution.append(null_counts)
    sum_ = sum(null_elem >= max_count for null_elem in null_distribution)
    p_value = (sum_ + 1) / (num_perm + 1)
    return p_value