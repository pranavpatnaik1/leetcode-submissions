class Solution:
    def validPalindrome(self, s: str) -> bool:
    
        l, r = 0, len(s) - 1
        valid = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                check_l = s[l+1:r+1]
                check_r = s[l:r]
                return check_l == check_l[::-1] or check_r == check_r[::-1]
                
        
        return True