import os
from datasets import datasets
from FrequentKmers import FrequentKmers
from task2 import tree_by_neighbor_joining

def get_files(dir_path):
  res = []
  for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
      res.append(path)
  return res

def most_frequent_nine_mer(nine_mers_dict):
  max_value = 0
  max_key = None
  for index,value in enumerate(nine_mers_dict):
    if nine_mers_dict[value] > max_value:
      max_value = nine_mers_dict[value]
      max_key = value
  return max_key

def retrive_nine_mers(dir_path):
  fk = FrequentKmers()
  #dir_path = './genomes/Coronavirus'
  files = get_files(dir_path)
  covid_k = [9]
  nine_mers = {}
  for file in files: 
    covid2_genome = fk.get_covid_genome(dir_path + '/' + file)
    for k in covid_k:
      result = fk.better_frequent_words(covid2_genome, k)
      rs = result[0]
      r_len = len(result[0])
      if r_len < 1000:
        for r in rs:
          nine_mers[r] = nine_mers[r] + 1 if r in nine_mers else 1
          print("|", file, "|", k, "|", r, "|")
  return nine_mers

def get_all_mutations(kmer):
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
  nine_mers = retrive_nine_mers('./genomes/Coronavirus')
  nine_mer = most_frequent_nine_mer(nine_mers) #'TAAACGAAC'
  sequences = get_all_mutations(nine_mer)
  sequences.append(nine_mer)
  tree = tree_by_neighbor_joining(sequences, True)
  

  ['AAAACGAAC' 'CAAACGAAC' 'GAAACGAAC' 'TAAAAGAAC' 'TAAACAAAC' 'TAAACCAAC'
 'TAAACGAAA' 'TAAACGAAG' 'TAAACGAAT' 'TAAACGACC' 'TAAACGAGC' 'TAAACGATC'
 'TAAACGCAC' 'TAAACGGAC' 'TAAACGTAC' 'TAAACTAAC' 'TAAAGGAAC' 'TAAATGAAC'
 'TAACCGAAC' 'TAAGCGAAC' 'TAATCGAAC' 'TACACGAAC' 'TAGACGAAC' 'TATACGAAC'
 'TCAACGAAC' 'TGAACGAAC' 'TTAACGAAC']