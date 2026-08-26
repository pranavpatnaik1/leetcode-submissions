class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def createAnagram(s): # helper: create anagrams
            ref = [0] * 26
            for c in s:
                ind = ord(c) - ord('a')
                ref[ind] += 1
            
            return tuple(ref)
        
        res = dict()
        for j in range(len(strs)): # each string
            anagram = createAnagram(strs[j])
            if anagram in res:
                res[anagram].append(strs[j])
            else:
                res[anagram] = [strs[j]]
        
        return list(res.values())
            


        