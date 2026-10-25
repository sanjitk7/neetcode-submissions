class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupe = {}

        for i in range(len(nums)):
            if nums[i] in dupe and i - dupe[nums[i]] <= k:
                return True
            dupe[nums[i]] = i
        
        return False
        