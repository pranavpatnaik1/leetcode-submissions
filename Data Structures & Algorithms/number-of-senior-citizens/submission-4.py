class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([age for age in details if int(age[11:13]) > 60 ])