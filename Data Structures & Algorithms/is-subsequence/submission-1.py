class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def checkSub(first, second):
            if first >= len(s):
                return True

            if second >= len(t):
                return False
            
            if s[first] == t[second]:
                return checkSub(first + 1, second + 1)
            else:
                return checkSub(first, second + 1)
        
        return checkSub(0, 0)
            


        