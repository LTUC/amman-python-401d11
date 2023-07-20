
'''
'd' -> 100 * 283 = 28300 % 1024 = 652
'''

from hash_map import HashTable


def test_hash_method():
  expected = 652
  hash = HashTable()
  actual = hash._HashTable__hash('d')
  assert expected == actual


# (DS._DataScience__PrintMeNot()