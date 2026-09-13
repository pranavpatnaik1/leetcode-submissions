class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, currPartition = [], []

        def dfs(i, j):
            if j >= len(s):
                if j == i:
                    res.append(currPartition.copy())
                return
            
            currString = s[i:j + 1]
            if currString == currString[::-1]:
                currPartition.append(currString)
                dfs(j + 1, j + 1)
                currPartition.pop()

            dfs(i, j + 1)
        
        dfs(0, 0)
        return res