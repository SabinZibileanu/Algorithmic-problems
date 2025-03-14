from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1

        while (left < right) and (right < len(nums)):
            
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            
            elif (nums[left] != 0 and nums[right] == 0) or (nums[left] != 0 and nums[right] != 0):
                left += 1
                right += 1
            
            elif nums[left] == 0 and nums[right] == 0:
                right += 1
        print(nums)




        