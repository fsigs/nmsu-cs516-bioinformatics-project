from FrequentKmers import FrequentKmers

if __name__ == '__main__':
  fk = fk = FrequentKmers()
  print("===============================")
  print("Part 1: Frequent Words counting")
  print("===============================")
  frequent_words = fk.frequent_words("ACGTTTCACGTTTTACGG", 3)
  print(frequent_words)

  #see slide ch1 64
  print("===============================")
  print("Part 2: Frequent Words hashing")
  print("===============================")
  frequent_words = fk.better_frequent_words("ACGTTTCACGTTTTACGG", 3)
  print(frequent_words)

  print("===============================")
  print("Part 3: Generating Sequence")
  print("===============================")
  sequence = fk.generate_dna(10)
  print(sequence)