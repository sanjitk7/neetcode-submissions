import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        heap = list()
        for key,v in d.items():
            heapq.heappush(heap,(v,key))
        heapq.heapify_max(heap)
        
        result = []

        for i in range(k):
            element = heapq.heappop_max(heap)
            result.append(element[1])
        
        return result


        