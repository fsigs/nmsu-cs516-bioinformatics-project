import unittest
from FrequentKmers import FrequentKmers

class FrequentKmersTests(unittest.TestCase):
  
  def better_frequent_words_test01(self):
    fk = FrequentKmers()
    text = "ACGTTTCACGTTTTACGG"
    k = 3
    expected = ["ACG","TTT"]
    actual = fk.better_frequent_words(text, k)
    self.assertEqual(actual, expected)

