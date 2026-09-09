class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def findCombination(currList, pos, remaining):
            if remaining == 0:
                res.append(currList.copy())
                return
            
            if remaining < 0 or pos >= len(candidates):
                return
            
            next_pos = pos + 1
            while next_pos < len(candidates) and candidates[next_pos] == candidates[pos]:
                next_pos += 1
            

            findCombination(currList + [candidates[pos]], pos + 1, remaining - candidates[pos])
            findCombination(currList, next_pos, remaining)
        
        findCombination([], 0, target)

        return res