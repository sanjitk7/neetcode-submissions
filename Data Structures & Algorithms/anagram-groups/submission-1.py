from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outerDict = defaultdict(list)
        for s in strs:
            d = defaultdict(int)
            for x in s:
                d[x]+=1
            key = tuple(sorted(d.items()))
            outerDict[key].append(s)
        return list(outerDict.values())