class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count = dict()

        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i], 0) + 1
        
        updateCount = dict()

        l, r = 0, len(s1) - 1

        for i in range(len(s1)):
            updateCount[s2[i]] = updateCount.get(s2[i], 0) + 1

        while r < len(s2):
            print(updateCount.items())
            if updateCount.items() <= count.items():
                return True
            
            updateCount[s2[l]] -= 1
            if updateCount[s2[l]] == 0:
                del updateCount[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                updateCount[s2[r]] = updateCount.get(s2[r], 0) + 1
        
        return False
            

            