
import sys
from timeit import default_timer as timer
from DiGraph import DiGraph
from sequence import random_DNA_sequence, get_kmers, compare_composition
from deBrujinByString import create_deBruijn_graph_by_string_comp
from deBrujinByHash import create_deBruijn_graph_by_hashing
from EulerPath import has_Eulerian_path, find_Eulerian_path
from k_assembler import build_sequence,assemble_kmers
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def test_and_print_message(seq, seq_truth, k, message):
  if seq == seq_truth:
    msg = "Passed " + message + " (assembled original sequence). Congratulations!"
    print("\033[32m{}\033[0m".format(msg))
  elif compare_composition(seq, seq_truth, k):
    msg = "Passed " + message + " (assembled a sequence of the same composition with the original sequence). Congratulations!"
    print("\033[32m{}\033[0m".format(msg))
  else:
    sys.stderr.write("\033[31m{}\033[0m".format("FAILED test!\n"))

def test_1(method):
  print("\033[33m{}\033[0m".format("Test 1"))
  print("\033[33m{}\033[0m".format("======"))
  print(f"Testing k-assembler by {method}")
  
  # Testing sequences:
  seqs_truth = [
    "aaaaaaaaaaa",
    "agcagctcagc",
    "agcagctcagg",
    random_DNA_sequence(10000, 20000)
  ]
  
  # The value of k for k-mers to be used for each test sequence:
  ks = [5, 3, 3, 20]
  
  for i in range(len(seqs_truth)):
    print(f"\nExample {i}:")
    
    seq_truth = seqs_truth[i]
    k = ks[i]
    kmers = get_kmers(seq_truth, k, True)
    g = DiGraph()

    begin = timer()
    if method == "k-mer pairwise comparison":
      g = create_deBruijn_graph_by_string_comp(kmers, g)
    elif method == "k-mer hashing":
      g = create_deBruijn_graph_by_hashing(kmers, g)
    else:
      sys.stderr.write("ERROR: unknown method!\n")
      return
    end = timer()
    elapsed_secs = round((end - begin) * 1000, 3)

    print(f"Elapsed time for building de Bruijn graph: {elapsed_secs}")
    
    if has_Eulerian_path(g):
      print("\033[32m{}\033[0m".format("Passed test for existence of Eulerian path. Congratulations!"))
    else:
      print("\033[31m{}\033[0m".format("Failed test for existence of Eulerian path!"))
    
    try:
      path = find_Eulerian_path(g)
      seq = build_sequence(path, g)
      message = f"Test 1 Example {i}"
      test_and_print_message(seq, seq_truth, k, message) 
    except Exception as e:
      sys.stderr.write(f"ERROR: {e}\n")
      return


def test_2(method):
  print("\033[33m{}\033[0m".format("Test 2"))
  print("\033[33m{}\033[0m".format("======"))
  seq_truth = random_DNA_sequence()
  k = 10
  kmers = get_kmers(seq_truth, k)
  try:
      seq = assemble_kmers(kmers, method)
      test_and_print_message(seq, seq_truth, k, "Test 2")
  except Exception as e:
      print(e)

def test_3(method):
  print("\033[33m{}\033[0m".format("Test 3"))
  print("\033[33m{}\033[0m".format("======"))
  seq_truth = random_DNA_sequence(15, 15)
  k = 4
  print("Sequence:", seq_truth)
  kmers = get_kmers(seq_truth, k)
  print("kmers:")
  for kmer in kmers:
      print(kmer)
  try:
      seq = assemble_kmers(kmers, method, "deBruijn.dot")
      test_and_print_message(seq, seq_truth, k, "Test 3")
  except Exception as e:
      print(e)

def generate_chart(method):
  print()
  print("\033[33m{}\033[0m".format("Output for report"))
  print("\033[33m{}\033[0m".format("=================="))
  ks = [3, 5, 7, 9, 11, 13, 15, 17, 19]
  seqs_truth = [
    random_DNA_sequence(100, 500),
    random_DNA_sequence(100, 1000),
    random_DNA_sequence(1000, 2000),
    random_DNA_sequence(1000, 3000),
    random_DNA_sequence(1000, 4000),
    random_DNA_sequence(1000, 5000),
    random_DNA_sequence(1000, 6000),
    random_DNA_sequence(1000, 7000),
    random_DNA_sequence(1000, 8000)
  ]

  run_times = []
  for i in range(len(seqs_truth)):
    seq_truth = seqs_truth[i]
    k = ks[i]
    kmers = get_kmers(seq_truth, k, True)
    g = DiGraph()
    begin = timer()
    if method == "k-mer pairwise comparison":
      g = create_deBruijn_graph_by_string_comp(kmers, g)
    elif method == "k-mer hashing":
      g = create_deBruijn_graph_by_hashing(kmers, g)
    else:
      sys.stderr.write("ERROR: unknown method!\n")
      return
    end = timer()
    elapsed_secs = round((end - begin) * 1000, 3)
    run_times.append(elapsed_secs)

  data = {'k':ks,'run_time':run_times}
  df = pd.DataFrame(data)
  sns.lineplot(data=df, x='k', y='run_time')
  plt.xlabel('K')
  plt.ylabel('Run Time (secs)')
  plt.title('Method: ' + method.upper())
  png_file_name = method.lower().replace(" ", "-")
  plt.savefig("../docs/images/" + png_file_name + '.png')
  print("Report plots have been generated in /docs/images folder...\n")

  print("|Language|Method|K-length|Run time (secs)|")
  print("|:----:|:----:|:---:|:-----:|")
  for i in range(0,len(ks)):
    print("|Python|",method,"|",ks[i],"|",run_times[i])

  
def test_seq_assembly():
  methods = [
    "k-mer pairwise comparison",
    "k-mer hashing"
  ]
  for method in methods:
    print()
    test_1(method)
    print()
    test_2(method)
    print()
  test_3("k-mer hashing")

  for method in methods:
    generate_chart(method)
  
