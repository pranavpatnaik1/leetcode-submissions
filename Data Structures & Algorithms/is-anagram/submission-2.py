class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def createAnagram(s: str):
            ref = dict()
            for i in s:
                if i in ref:
                    ref[i] += 1
                else:
                    ref[i] = 1

            return ref
        
        return createAnagram(s) == createAnagram(t)
        