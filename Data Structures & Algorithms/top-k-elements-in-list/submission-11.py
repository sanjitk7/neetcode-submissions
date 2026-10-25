import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        heap = list()
        heapq.heapify_max(heap)
        for key,v in d.items():
            heapq.heappush_max(heap,(v,key))
        
        result = []

        for i in range(k):
            element = heapq.heappop_max(heap)
            result.append(element[1])
        
        return result


        