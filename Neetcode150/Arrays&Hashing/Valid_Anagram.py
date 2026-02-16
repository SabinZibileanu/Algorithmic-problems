from collections import Counter

# O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        allLetts = set(list(s) + list(t))
        s_lett_freq = Counter(s)
        t_lett_freq = Counter(t)


        for lett in allLetts:
            if s_lett_freq[lett] != t_lett_freq[lett]:
                return False
        
        return True

# O(nmlogn)
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        for l1, l2 in zip(sorted(s), sorted(t)):
            if l1 != l2:
                return False
        
        return True
        

