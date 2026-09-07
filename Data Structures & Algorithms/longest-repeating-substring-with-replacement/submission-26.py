class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        count = dict()
        l, r = 0, 0
        maxLength = 0
        while r < len(s): 
            currLength = ((r - l) + 1)
            
            count[s[r]] = count.get(s[r], 0) + 1
            currTarget = max(count.values())

            numReplacements = ((r - l) + 1) - currTarget
            if numReplacements <= k:
                currLength = ((r - l) + 1)
                maxLength = max(maxLength, currLength)
                r += 1
            else:
                while numReplacements > k:
                    count[s[l]] -= 1
                    currTarget = max(count.values())
                    l += 1

                    numReplacements = ((r - l) + 1) - currTarget

                maxLength = max(maxLength, (r - l) + 1)
                r += 1

        return maxLength



                


