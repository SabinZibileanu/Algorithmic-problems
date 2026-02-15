from collections import Counter, deque
from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxHeap = [-freq for freq in taskCount.values()]
        heapify(maxHeap)
        time = 0
        q = deque() 

        while maxHeap or q:
            time += 1
            if maxHeap:
                val = heappop(maxHeap)
                if val + 1:  
                    q.append((val  + 1, time + n ))
            
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
        
        return time



# Another attempt (does not work)
        # tasksFreq = Counter(tasks)
        # maxTasks = 0
        # for task in tasksFreq:
        #     maxTasks += tasksFreq[task] * n
        
        # cycles = ['_'] * 10**5
        # slow = 0
        # fast = 0
        # for lett in tasksFreq:
        #     for i in range(tasksFreq[lett]):
        #         cycles[fast] = lett
        #         fast += n + 1
            
        #     slow += 1
        #     fast = slow
        
        # # get the last idx
        # print(cycles)
        # for idx, char in enumerate(cycles):
        #     if char in tasksFreq:
        #         lastIdx = idx
        
        # return len(cycles[:lastIdx + 1])