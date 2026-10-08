class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        count = 0

        if len(s) == 1:
            return 1

        for i in range(len(s)):
            dp[i][i] = 1
            count += 1

        for length in range(2, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if j - i <= 1:
                    dp[i][j] = s[i] == s[j]
                    if dp[i][j]:
                        count += 1
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                    if dp[i][j]:
                        count += 1
        
        return count
                    

