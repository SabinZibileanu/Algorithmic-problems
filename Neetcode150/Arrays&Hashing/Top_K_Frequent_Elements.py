from heapq import heapify, heappop
from typing import List
from collections import Counter


# O(n) bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        numsFreq = Counter(nums)
        buckets = [[] for num in range(len(nums) + 1)]
        for num, freq in numsFreq.items():
            buckets[freq].append(num)
        
        
        for idx in range(len(buckets) - 1, -1, -1):
            if buckets[idx]:
                for num in buckets[idx]:
                    res.append(num)
                    if len(res) == k:
                        return res

# O(klogn) maxheap
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = [(-freq, num) for num, freq in Counter(nums).items()]
        heapify(maxHeap)
        res = []

        while k:
            val = heappop(maxHeap)
            res.append(val[1])
            k -= 1
        
        return res

# O(nlogn)
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFreq = Counter(nums)
        frequencies = sorted(numsFreq, key = numsFreq.get, reverse = True)[:k]
        
        return frequencies