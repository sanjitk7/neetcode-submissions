class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        length = 0
        for i in a:
            if (i - 1) not in a:
                b = 1
                while (i + b) in a:
                    b += 1
                length = max(length, b)
        return length