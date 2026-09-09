class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def findParens(currList, opening, closing):
            if opening == closing and opening == n:
                res.append("".join(currList))
                return
            
            if opening > closing and opening == n:
                findParens(currList + [")"], opening, closing + 1)

            if opening > closing and opening < n:
                findParens(currList + ["("], opening + 1, closing)
                findParens(currList + [")"], opening, closing + 1)
            
            if opening == closing:
                findParens(currList + ["("], opening + 1, closing)
                
                
            
        
        findParens([], 0, 0)
        return res

