class Solution:
    
    def encode(self, strs):
        res = ""
        for i in strs:
            res += str(len(i)) + "/" + i
        return res
    
    def decode(self, string):
        res = []
        i = 0

        while i < len(string):
            j = i
            while string[j] != "/":
                j += 1
            count = int(string[i:j])
            i = j + 1
            j = i + count
            res.append(string[i:j])
            i = j
        
        return res
