class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ","")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)
        return s[::-1] == s