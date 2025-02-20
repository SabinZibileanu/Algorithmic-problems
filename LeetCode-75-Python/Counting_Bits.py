from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            binary_number = bin(i)
            result.append(binary_number.count('1'))

        return result

