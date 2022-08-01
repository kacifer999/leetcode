class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        c1 = Counter(s1)
        left = 0
        res = False
        if len(s1) > len(s2):return False
        while left + len(s1) <= len(s2):
            c2 = Counter(s2[left:left + len(s1)])
            if c1 == c2:
                res = True
            left +=1
        return res

#######
print(Solution().checkInclusion(s1 = 'ab',s2 = 'eidbaooo'))