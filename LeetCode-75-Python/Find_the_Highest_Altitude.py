from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr_gains = [0]
        distance = 0

        for gain_point in gain:
            distance += gain_point
            arr_gains.append(distance)
        
        return max(arr_gains)
