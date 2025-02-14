from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i] # cool trick for sliding window: instead of calculating the sum for each subarray, extract the first element of the previous window and add the next element
            max_sum = max(current_sum, max_sum)
        
        return max_sum / k

          