from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = right_sum = 0
        arr_left = []
        arr_right = []
        counter_occurences = 0

        for i in range(len(nums)):
            left_sum += nums[i]
            arr_left.append(left_sum)
        
        for i in range(len(nums) - 1, -1, -1):
            right_sum += nums[i]
            arr_right.append(right_sum)
        
        print(arr_left, arr_right[::-1])
        for num_left, num_right in zip(arr_left, arr_right[::-1]):
            if num_left == num_right:
                return counter_occurences
            counter_occurences += 1
        
        return -1
