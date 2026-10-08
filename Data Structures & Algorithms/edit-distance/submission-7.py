class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        res = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if (i == 0):
                    res[i][j] = j 
                elif (j == 0):
                    res[i][j] = i
                
            
                elif word1[i-1] == word2[j-1]:
                    res[i][j] = res[i-1][j-1]
                
                else:
                    res[i][j] = min(res[i-1][j] + 1, res[i][j-1] + 1, res[i-1][j-1] + 1)
        
        return res[len(word1)][len(word2)]