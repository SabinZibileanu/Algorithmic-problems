from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        nr_possible_divisions = len(nums) // 2

        sorted_array = sorted(nums)
        counter_operations = 0

        while (left_pointer < right_pointer) and (counter_operations < nr_possible_divisions):
            if sorted_array[left_pointer] + sorted_array[right_pointer] < k:
                left_pointer += 1
            
            elif sorted_array[left_pointer] + sorted_array[right_pointer] > k:
                right_pointer -= 1
            
            else:
                counter_operations += 1
                left_pointer += 1
                right_pointer -= 1
        
        return counter_operations
