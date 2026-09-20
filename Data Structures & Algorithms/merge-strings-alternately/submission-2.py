class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        f, s = 0, 0
        while f <= len(word1) - 1 and s <= len(word2) - 1:
            res += word1[f] + word2[s]
            s += 1
            f += 1
        
        if word1[f:]:
            res += word1[f:]
        if word2[s:]:
            res += word2[s:]

        return res