class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if not c.isalnum():
                continue
            elif c.isupper():
                res += c.lower()
            else:
                res += c
        
        return res[::-1] == res

        