class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in s:
            if i.isalnum():
                a.append(i.lower())
        for j in range(len(a) // 2):
            if a[j] != a[len(a) - j - 1]:
                return False
        return True