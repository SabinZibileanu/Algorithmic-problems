from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenValues = set()
        for num in nums:
            if num in seenValues:
                return True
            
            seenValues.add(num)
        
        return False