from typing import List

# the time complexity can be reduced to O(1) by using 2 pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        # getting the prefix and the suffix max
        def getMaximum(arr):
            absMax = 0
            maxes = []
            for idx, val in enumerate(arr):
                if idx == 0:
                    maxes.append(absMax)
                    absMax = max(absMax, val)
                    continue
            
                currMax = max(absMax, val)
                if currMax != absMax:
                    maxes.append(absMax)
                    absMax = currMax
                    continue
                
                maxes.append(absMax)

            return maxes
        
        prefixMax = getMaximum(height)
        suffixMax = getMaximum(height[::-1])[::-1]
        totalQty = 0

        for idx, h in enumerate(height):
            minMaxes = min(prefixMax[idx], suffixMax[idx])
            possibleQty = minMaxes - h
            if possibleQty > 0:
                totalQty += possibleQty

        return totalQty


        
        