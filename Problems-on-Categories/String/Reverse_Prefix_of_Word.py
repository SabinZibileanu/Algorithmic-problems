class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
          return word
        idx_ch = word.index(ch)
        substring_reversed = word[0:idx_ch + 1][::-1]
        remainder = word[idx_ch + 1: ]

        return substring_reversed + remainder