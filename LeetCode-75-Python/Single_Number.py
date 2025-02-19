from typing import List

# HashMap approach (most intuitive)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:

#         hash_map_frequency = {}

#         for number in nums:
#             if number not in hash_map_frequency:
#                 hash_map_frequency[number] = 1
#             else:
#                 hash_map_frequency[number] += 1
        
#         for key,value in hash_map_frequency.items():
#             if value == 1:
#                 return key

# XOR approach
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor