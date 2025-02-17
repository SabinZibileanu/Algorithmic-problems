class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result_merged = ""
        left = right = 0

        while left < len(word1) and right < len(word2):
            result_merged += word1[left] + word2[right]
            left += 1
            right += 1
        
        if left == len(word1) and right == len(word2):
            return result_merged
        
        elif left < len(word1):
            return result_merged + word1[left:]
        
        elif right < len(word2):
            return result_merged + word2[right:]


# One liner with reduce and itertools zip_longeest (very cool trick)
# from functools import reduce
# from itertools import zip_longest

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         return ''.join(reduce(lambda a, b: a+b, zip_longest(word1, word2, fillvalue = '')))


