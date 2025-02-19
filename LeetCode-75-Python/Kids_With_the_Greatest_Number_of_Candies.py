from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum_number_candies = max(candies)
        result_arr = []

        for nr_candy in candies:
            
            if nr_candy + extraCandies >= maximum_number_candies:
                result_arr.append(True)
            
            else:
                result_arr.append(False)
        
        return result_arr
        