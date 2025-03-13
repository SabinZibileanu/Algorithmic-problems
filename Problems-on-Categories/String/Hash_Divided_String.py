import string

class Solution:
    def stringHash(self, s: str, k: int) -> str:
      alphabet_letters = list(string.ascii_lowercase)
      letters_mapping = {}
      inversed_letters_mapping = {}
      start_point = 0
      result = ""
      auxiliary_k = k

      for i, letter in enumerate(alphabet_letters):
        letters_mapping[letter] = i
        inversed_letters_mapping[i] = letter
      
      while k <= len(s):
        substring = s[start_point : k]
        sum_hash_values = sum([letters_mapping[char] for char in substring])
        result += inversed_letters_mapping[sum_hash_values % 26]

        start_point += auxiliary_k
        k += auxiliary_k
      
      return result