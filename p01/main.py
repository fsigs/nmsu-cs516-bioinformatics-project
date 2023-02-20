from FrequentKmers import FrequentKmers

if __name__ == '__main__':
  fk = fk = FrequentKmers()
  #see slide ch1 64
  print("Part 2: Frequent Words")
  frequent_words = fk.better_frequent_words("ACGTTTCACGTTTTACGG", 3)
  print(frequent_words)

  print("Part 3: Generating Sequence")
  sequence = fk.generate_dna(10)
  print(sequence)