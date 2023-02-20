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

  print("===============================")
  print("Part 4: Ploting runtime for K & L")
  print("===============================")
  print("Pending....")

  print("===============================")
  print("Part 5: Reading Covid Genome")
  print("===============================")
  genome = fk.get_covid_genome()
  k_values = [3, 6, 9, 12, 15]
  for k in k_values:
    print(f"Frequent {k}-mers ")
    print("****************** ")
    print(fk.better_frequent_words(genome, k))
  