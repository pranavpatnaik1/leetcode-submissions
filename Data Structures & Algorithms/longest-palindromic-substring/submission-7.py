class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [[False] * len(s) for _ in range(len(s))]

        best_start = 0
        best_len = 1

        for i in range(len(s)):
            res[i][i] = True
        
        for length in range(2, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1

                if length == 2:
                    res[i][j] = (s[i] == s[j])
                else:
                    res[i][j] = (s[i] == s[j]) and res[i+1][j-1]
        
                if res[i][j] and length > best_len:
                    best_start = i
                    best_len = length
        
        return s[best_start:best_start + best_len]

