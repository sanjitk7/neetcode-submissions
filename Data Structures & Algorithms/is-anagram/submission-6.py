from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = defaultdict(int), defaultdict(int)
        for x in s:
            d1[x] += 1
        for y in t:
            d2[y] += 1
            
        return d1 == d2