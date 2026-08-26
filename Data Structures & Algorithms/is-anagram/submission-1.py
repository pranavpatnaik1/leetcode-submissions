class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def createCount(targ):
            ref = dict()
            for i in range(len(targ)):
                if targ[i] not in ref:
                    ref[targ[i]] = 1
                else:
                    ref[targ[i]] += 1
            
            return ref
        
        return createCount(s) == createCount(t)
        