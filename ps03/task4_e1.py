#from datasets import datasets

import os
from FrequentKmers import FrequentKmers
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
  print("| Genome | k-mer | Sequence |")
  for file in files: 
    covid2_genome = fk.get_covid_genome(dir_path + '/' + file)
    for k in covid_k:
      result = fk.better_frequent_words(covid2_genome, k)
      rs = result[0]
      r_len = len(result[0])
      if r_len < 1000:
        for r in rs:
          nine_mers[r] = nine_mers[r] + 1 if r in nine_mers else 1
          print(f"| {file} | {k}-mer | {r} |")
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
  
  klength = 9
  type_drawing = "ascii"
  print()
  print("Coronavirus")
  print("===========")
  nine_mers = get_kmers('./genomes/Coronavirus',klength)
  sequences = get_sequences(nine_mers)
  most_frequent_nine_mer = get_most_frequent_nine_mer(nine_mers)
  print(f'\n* Most frequent {klength}-mer: ',most_frequent_nine_mer[0],'. Ocurrences: ',str(most_frequent_nine_mer[1]),'in studied genomes\n')
  tree = tree_by_neighbor_joining(sequences, True, type_drawing)
  print()

  exit()
  print("HIV-1")
  print("=====")
  nine_mers = get_kmers('./genomes/HIV-1',klength)
  sequences = get_sequences(nine_mers)
  most_frequent_nine_mer = get_most_frequent_nine_mer(nine_mers)
  print(f'\n* Most frequent {klength}-mer: ',most_frequent_nine_mer[0],'. Ocurrences: ',str(most_frequent_nine_mer[1]),'in studied genomes\n')
  tree = tree_by_neighbor_joining(sequences, True, type_drawing)
 
  print("Adenovirus-2")
  print("============")
  nine_mers = get_kmers('./genomes/Adenovirus-2',klength)
  sequences = get_sequences(nine_mers)
  most_frequent_nine_mer = get_most_frequent_nine_mer(nine_mers)
  print(f'\n* Most frequent {klength}-mer: ',most_frequent_nine_mer[0],'. Ocurrences: ',str(most_frequent_nine_mer[1]),'in studied genomes\n')
  tree = tree_by_neighbor_joining(sequences, True, type_drawing)

  print("Ebola")
  print("=====")
  nine_mers = get_kmers('./genomes/Ebola',klength)
  sequences = get_sequences(nine_mers)
  most_frequent_nine_mer = get_most_frequent_nine_mer(nine_mers)
  print(f'\n* Most frequent {klength}-mer: ',most_frequent_nine_mer[0],'. Ocurrences: ',str(most_frequent_nine_mer[1]),'in studied genomes\n')
  tree = tree_by_neighbor_joining(sequences, True, type_drawing)

  print("Hepatitis-B")
  print("===========")
  nine_mers = get_kmers('./genomes/Hepatitis-B',klength)
  sequences = get_sequences(nine_mers)
  most_frequent_nine_mer = get_most_frequent_nine_mer(nine_mers)
  print(f'\n* Most frequent {klength}-mer: ',most_frequent_nine_mer[0],'. Ocurrences: ',str(most_frequent_nine_mer[1]),'in studied genomes\n')
  tree = tree_by_neighbor_joining(sequences, True, type_drawing)

  print("Diabetes")
  print("===========")
  nine_mers = get_kmers('./genomes/Diabetes',klength)
  sequences = get_sequences(nine_mers)
  most_frequent_nine_mer = get_most_frequent_nine_mer(nine_mers)
  print(f'\n* Most frequent {klength}-mer: ',most_frequent_nine_mer[0],'. Ocurrences: ',str(most_frequent_nine_mer[1]),'in studied genomes\n')
  tree = tree_by_neighbor_joining(sequences, True, type_drawing)