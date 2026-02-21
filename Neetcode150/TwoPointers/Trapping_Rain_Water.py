from typing import List

# the space complexity can be reduced to O(1) by using 2 pointers
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


# O(1) space

class Solution2:
    def trap(self, height: List[int]) -> int:
        totalQty = 0
        left, right = 0, len(height) - 1
        currLeftMax = height[left]
        currRightMax = height[right]
        
        while left < right:
            if currLeftMax < currRightMax:
                left += 1
                currLeftMax = max(currLeftMax, height[left])
                totalQty += currLeftMax - height[left]
            
            else:
                right -= 1
                currRightMax = max(currRightMax, height[right])
                totalQty += currRightMax - height[right]

        return totalQty


        
        