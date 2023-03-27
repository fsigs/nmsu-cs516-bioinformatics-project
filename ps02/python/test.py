
import sys
from timeit import default_timer as timer
from DiGraph import DiGraph, Node
from sequence import random_DNA_sequence, get_kmers, compare_composition
from deBrujinByString import create_deBruijn_graph_by_string_comp
from deBrujinByHash import DNAHasher, create_deBruijn_graph_by_hashing
from EulerPath import has_Eulerian_path, find_Eulerian_path
from k_assembler import build_sequence,assemble_kmers

def test_and_print_message(seq, seq_truth, k, message):
  #print(seq, seq_truth)
  if seq == seq_truth:
    print("Passed", message, "(assembled original sequence). Congratulations!")
  elif compare_composition(seq, seq_truth, k):
    print("Passed", message, "(assembled a sequence of the same composition with the original sequence). Congratulations!")
  else:
    sys.stderr.write("FAILED test 1!\n")

def test_1(method):
  print(f"Testing k-assembler by {method}")
  
  # Testing sequences:
  seqs_truth = [
    "aaaaaaaaaaa",
    "agcagctcagc",
    "agcagctcagg",
    random_DNA_sequence(10000, 20000) #(10000, 20000)
  ]
  
  # The value of k for k-mers to be used for each test sequence:
  ks = [5, 3, 3, 20]
  
  for i in range(len(seqs_truth)):
    print(f"\nExample {i}:")
    
    seq_truth = seqs_truth[i]
    k = ks[i]
    kmers = get_kmers(seq_truth, k, True)
    #print("seq_truth: ", seq_truth, ". k=",k)
    #print("kmers: ", kmers)
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
    elapsed_secs = round((end - begin) * 1000, 2)

    #print("method: ", method)
    print(f"Elapsed time for building de Bruijn graph: {elapsed_secs}")
    #g.print()
    if has_Eulerian_path(g):
      print("Passed test for existence of Eulerian path. Congratulations!")
    else:
      print("Failed test for existence of Eulerian path!")
    #try:
    path = find_Eulerian_path(g)
    seq = build_sequence(path, g)
    message = f"Test 1 Example {i}"
    test_and_print_message(seq, seq_truth, k, message)
    '''
    except Exception as e:
      sys.stderr.write(f"ERROR: {e}\n")
      return
      '''

def test_2(method):
  seq_truth = random_DNA_sequence()
  k = 10
  kmers = get_kmers(seq_truth, k)
  try:
      seq = assemble_kmers(kmers, method)
      test_and_print_message(seq, seq_truth, k, "Test 2")
  except Exception as e:
      print(e)

def test_3(method):
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


def test_seq_assembly():
  methods = [
    "k-mer pairwise comparison",
    "k-mer hashing"
  ]
  for method in methods:
    print("-----------")
    test_1(method)
    print()
    #test_2(method)
    #print()
  #print("-----------")
  #test_3("k-mer hashing")

