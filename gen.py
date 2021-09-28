import random, string, sys, os


def create_random_txt(FILE = sys.stdout):
  print("boo", file = FILE)

def create_random_fasta(FILE = sys.stdout):
  kinds = "cat cat dog dog dog mouse fly".split()
  what = random.choice(kinds)
  id = ''.join(random.choices(string.ascii_letters + string.digits, k = 20))
  seq = [''.join(random.choices("ACGT", k = 60)) for n in range(random.randint(5, 10))] + [''.join(random.choices("ACGT", k = random.randint(1, 60))) ]

  print(f"> {what} {id}", file = FILE)
  print(*seq, sep = "\n", file = FILE)

folders = {'rui' : {'fasta' : 57, 'txt' : 22}, 'francisco': {'fasta': 22, 'txt' : 39}}
for D in folders:
  os.makedirs(D, exist_ok = True)
  for n in range(folders[D]['fasta']):
    with open(f"{D}/seq{n + 1:02}.fasta", "w") as F:
      create_random_fasta(F)
  for n in range(folders[D]['txt']):
    with open(f"{D}/f{n + 1:02}.txt", "w") as F:
      create_random_txt(F)
