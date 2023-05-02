from datasets import datasets

def print_table_datasets():
  dsks = [k for k in datasets.keys()]
  print("| Virus Type | Fasta Genome |  Title |")
  print("|:----------:|:------------:|:-------|")
  for dsk in dsks:
    for vsk in datasets[dsk].keys():
      print(f"| {dsk} | {vsk} | {datasets[dsk][vsk]['title']} |")

if __name__ == '__main__':
  print_table_datasets()