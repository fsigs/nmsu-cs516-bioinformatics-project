import pprint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from FrequentKmers import FrequentKmers

if __name__ == '__main__':
  
  pp = pprint.PrettyPrinter(indent=2)
  fk = fk = FrequentKmers()

  print()
  print("============================================")
  print("Task 1: Algorithm Frequent Words (counting)")
  print("============================================")
  print("Using test cases from class slides (Ch 1 slides 64 and 99), "
        "\nwe show the list of frequent words and running time in ms for our implementation are correct:")
  #test case: from slide 64 ch1 ppt
  frequent_words = fk.frequent_words("ACGTTTCACGTTTTACGG", 3)
  pp.pprint(frequent_words)
  #test case: from slide 99 ch1 ppt
  frequent_words = fk.frequent_words("atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc", 9)
  pp.pprint(frequent_words)

  print()
  print("=================================================")
  print("Task 2: Algorithm Better Frequent Words (hashing)")
  print("=================================================")
  print("Using test cases from class slides (Ch 1 slides 64 and 99)," 
        "\nwe show the list of frequent words and running time in ms for our implementation are correct:")
  #test case: from slide 64 ch1 ppt
  frequent_words = fk.better_frequent_words("ACGTTTCACGTTTTACGG", 3)
  pp.pprint(frequent_words)
  #test case: from slide 99 ch1 ppt
  frequent_words = fk.better_frequent_words("atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc", 9)
  pp.pprint(frequent_words)

  print()
  print("========================================")
  print("Task 3: Generating Random DNA Sequences")
  print("========================================")
  num_executions = 10
  random_length = 10
  print(f"Using Numpy random choice function of Python,\nwe generate {num_executions} random DNA sequences of variable lenght: ")
  for _ in range(num_executions):
    random_sequence = fk.generate_dna(np.random.randint(random_length, random_length + 5))
    pp.pprint(random_sequence)  
  
  print()
  print("=====================================================")
  print("Task 4: Ploting runtime comparing our two algorithms")
  print("=====================================================")
  dna_length = [25, 50, 75, 100, 250, 500, 750, 1000]
  dna_kmers = [3, 6, 9, 12, 15]
  print("Using Pandas and Matplot libraries of Python, \nwe plot the running time of our two algorithms \nfor different sequence lengths and different k-mers:")
  print("L = ", dna_length)
  print("K-mers = ", dna_kmers)
  
  random_results = []
  for l in dna_length:
    s = fk.generate_dna(l)
    pies_fwt = []
    pies_bfwt = []
    indexes = []
    for k in dna_kmers:
      result = {}
      result["l"] = l
      result["k"] = k
      fwt = fk.frequent_words(s, k)[1]
      result["fwt"] = fwt
      bfwt = fk.better_frequent_words(s, k)[1]
      result["bfwt"] = bfwt
      random_results.append(result)
      
      indexes.append(k)
      pies_fwt.append(fwt)
      pies_bfwt.append(bfwt)
    
    plotdata = pd.DataFrame({
      "runtime_fwt": pies_fwt,
      "runtime_bfwt": pies_bfwt
      }, index=indexes)

    ax = plotdata.plot(kind = "bar")
    for p in ax.patches:
      ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.title("Frequent and Best Frequent word time with L = " + str(l))
    plt.xlabel("K length")
    plt.ylabel("Runtime (ms)")
    plt.axhline(y=np.nanmean(fwt), color='blue', linestyle='--')
    plt.axhline(y=np.nanmean(bfwt), color='orange', linestyle='--')
    plt.savefig(f"./docs/images/q4_{l}.png", dpi=300)
    plt.show()

  print("\nNote: Images shown have been stored in docs/images folder to be embeded in the project.") 
  print("\nThe following is a table of the executions included in the charts:\n")
  print("|Length|K-length|FW(ms)|BFW(ms)|")
  print("|:----:|:---:|:-----:|:------:|")
  for r in random_results:
    print("|", r["l"], "|", r["k"], "|", r["fwt"], "|", r["bfwt"], "|") 
 
  print()
  print("============================================================")
  print("Tasks 5 and E2: SARS-CoV-2 and SARS-CoV most frequent k-mers")
  print("============================================================")
  
  print("\nThe following is a table of the most frequent k-mers present in the SARS-CoV-2 and SARS-CoV genomes:\n")
  print("|Genome|K-length|K-mer|")
  print("|:----:|:---:|:-----:|")
  file_names = ['SARS-CoV-2', 'SARS-CoV']
  covid_k = [3, 6, 9, 12, 15]
  for file in file_names: 
    covid2_genome = fk.get_covid_genome(file + '.txt')
    for k in covid_k:
      result = fk.better_frequent_words(covid2_genome, k)
      rs = result[0]
      for r in rs:
        print("|", file, "|", k, "|", r, "|")

  # Task 6
  # Use Blast:
  #  https://blast.ncbi.nlm.nih.gov/Blast.cgi
  #  https://www.youtube.com/watch?v=WRKQGwh_Mw0
  #  https://www.news-medical.net/health/How-Does-the-SARS-Virus-Genome-Compare-to-Other-Viruses.aspx

  print()
  print("================================================================================")
  print("E1: Null Distribution of the most frequent k-mers in SARS-CoV-2 genome sequence")
  print("================================================================================")
  covid2_genome = fk.get_covid_genome('SARS-CoV-2.txt')
  k_mer = 3
  num_per = 1000
  print(f"Using the SARS-CoV-2 genome sequence, our permutation test \nwith {num_per} permutations gives. We have considered a p-value threshld of 0.05 to decide \nif the most frequent k-mer is unlikely to have occurred by chance alone \nand consequently, it has biological significance:\n")
  for k_mer in covid_k:
    p_value = round(fk.permutation_test(covid2_genome, k_mer, num_per),5)
    if p_value < 0.05:
      bio_significance = "they DO HAVE biological significance"
    else:
      bio_significance = "they DO NOT HAVE biological significance"
    print(f"{k_mer}-mers give a p-value of {p_value}, then {bio_significance}")
  
  print()
  print("===========================================================================")
  print("E3: Find the longest k-mer repeats beyond 15 in SARS-CoV-2 genome sequence")
  print("===========================================================================")

  print()
  print("First, we find what is the max value for k in each Genome:\n")
  print("|Genome|K-length|# matches|")
  print("|:----:|:---:|:-----:|")
  file_names = ['SARS-CoV-2', 'SARS-CoV']
  covid_k = range(15,40)
  for file in file_names: 
    covid2_genome = fk.get_covid_genome(file + '.txt')
    for k in covid_k:
      result = fk.better_frequent_words(covid2_genome, k)
      rs = len(result[0])
      if rs < 1000:
        print("|", file, "|", k, "|", rs, "|")
  
  print("\nNow, that we know for SARS-CoV-2 is k=17 and for SARS-CoV is K=16, we found the longest kmers:")
  longest_covid2 = fk.better_frequent_words(fk.get_covid_genome(file_names[0] + '.txt'), 17)
  longest_covid1 = fk.better_frequent_words(fk.get_covid_genome(file_names[1] + '.txt'), 16)
  print("Longest k-mers in SARS-CoV-2: ", longest_covid2[0])
  print("Longest k-mers in SARS-CoV  : ", longest_covid1[0])
  print()

  exit()