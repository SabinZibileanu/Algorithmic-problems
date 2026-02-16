from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + '#' + word
        
        return encoded
    
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            currLength = int(s[i:j])
            res.append(s[j + 1: j + 1 + currLength])
            i = j + 1 + currLength
        
        return res

# kinda alternate solution (does not handle some edge cases, use the first one)
class Solution2:
    def encode(self, strs: List[str]) -> str:        
        if not strs:
            return 'None'
        encoded = ''
        for idx, word in enumerate(strs):
            if idx == len(strs) - 1:
                encoded += word
            
            else:
                encoded += word + self.delimeter
        
        return encoded
    
    def decode(self, s: str) -> List[str]:
        if s == 'None':
            return []
        return [char for char in s.split(self.delimeter)]