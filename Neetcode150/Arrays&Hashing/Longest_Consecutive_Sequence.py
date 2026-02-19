from typing import List

# best solution O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        uniqueNums = set(nums)

        for num in uniqueNums:
            currentLongest = 1

            if num - 1 not in uniqueNums: # this checks if num is the start of a sequence
                while num + 1 in uniqueNums:
                    currentLongest += 1
                    num += 1
            
            longest = max(longest, currentLongest)
        
        return longest

# alternate

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLongest = 0
        for num in nums:
            currLongest = 1
            while num + 1 in set(nums): # TLE
                currLongest += 1
                num += 1
            
            maxLongest = max(maxLongest, currLongest)

        
        return maxLongest
                

        
