class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range(len(nums)):
            a = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    a *= nums[j]
            output[i] = a
        return output