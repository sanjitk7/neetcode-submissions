import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       numSet = set(nums)
       result = 0

       for num in nums:
            if num-1 not in numSet:
                current_length = 0 
                while num+current_length in numSet:
                    current_length +=1
                result = max(current_length, result)
            # Skip other non starter sequence elements

       return result
