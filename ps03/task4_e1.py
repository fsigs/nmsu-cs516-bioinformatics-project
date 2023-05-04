import os
import sys
import numpy as np
from collections import Counter
from FrequentKmers import FrequentKmers
from datasets import datasets
from task2 import tree_by_neighbor_joining

def get_genome_files(dir_path):
  res = []
  for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
      res.append(path)
  return res

def get_most_frequent_nine_mer(nine_mers_dict):
  max_value = 0
  max_key = None
  for index,value in enumerate(nine_mers_dict):
    if nine_mers_dict[value] > max_value:
      max_value = nine_mers_dict[value]
      max_key = value
  return max_key, max_value

def get_kmers(dir_path, klength):
  fk = FrequentKmers()
  files = get_genome_files(dir_path)
  covid_k = [klength]
  
  nine_mers = {}
  lst = []
  for file in files: 
    covid2_genome = fk.get_covid_genome(dir_path + '/' + file)
    for k in covid_k:
      result = fk.better_frequent_words(covid2_genome, k)
      rs = result[0]
      r_len = len(result[0])
      if r_len < 1000:
        for r in rs:
          nine_mers[r] = nine_mers[r] + 1 if r in nine_mers else 1
          virus = dir_path.split('/')[len(dir_path.split('/')) - 1]
          dataset_virus = datasets[virus][file.replace(".txt", "")]["title"]
          l = {}
          l["v"] = dataset_virus
          l["k"] = k
          l["s"] = r
          lst.append(l)

  kmer_list = [d['s'] for d in lst]
  counter = Counter(kmer_list)
  sorted_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)
  
  print("| Sequence | Count | Genome |")
  print("|:---------|:-----:|:-------|")
  for s, count in sorted_counts:
    genome_titles = [d['v'] for d in lst if d['s'] == s]
    print(f"| {s} | {count} | {genome_titles} |")

  return nine_mers

def get_sequences(nine_mers):
  sequences = []
  for s in nine_mers.keys():
    sequences.append(s)
  return sequences

def generate_mutations(kmer):
  mutations = []
  nucleotides = ['A','C','T','G']
  for i in range(len(kmer)):
    for nucleotide in nucleotides:
      if kmer[i] != nucleotide:
        mutation = kmer[:i] + nucleotide + kmer[i+1:]
        if mutation not in mutations:
          mutations.append(mutation)
  return mutations

if __name__ == '__main__':
  
  klength = int(sys.argv[1]) if len(sys.argv) > 1 else 9
  type_drawing = "ascii"
  viruses = ['Coronavirus'] #['Coronavirus','HIV-1','Adenovirus-2','Ebola','Hepatitis-B']
  title = f"most frequent {klength}-mers"

  print()
  print("===========================================")
  print(f"Analysis of the {title}")
  print("===========================================")
  print()

  for virus in viruses:
    print(f"{virus} {title}")
    print("==========================================")
    nine_mers = get_kmers('./genomes/' + virus,klength)
    sequences = get_sequences(nine_mers)
    tree = tree_by_neighbor_joining(sequences, True, type_drawing)
    print('Runing time: {:.5f} seconds\n'.format(tree[1]))
    print()