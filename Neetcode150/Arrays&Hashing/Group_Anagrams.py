from typing import List
from collections import defaultdict

# O (m * n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCounts = defaultdict(list)

        for word in strs:
            charCount = [0] * 26
            
            for char in word:
                charCount[ord(char) - ord('a')] += 1
            
            charCounts[tuple(charCount)].append(word)
        
        return [group for group in charCounts.values()]

        
# O(m * n * logn)

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMapping = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))
            anagramsMapping[sortedWord].append(word)
        
        return [anagramsMapping[word] for word in anagramsMapping]
        