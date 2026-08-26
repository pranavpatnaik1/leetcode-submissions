class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 0
        maxLength = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            maxLength = max(r - l + 1, maxLength)
            seen.add(s[r])
            r += 1
        
        return maxLength
                
