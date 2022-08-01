class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import Counter
        res = []
        left = 0
        cp = Counter(p)
        if len(s) < len(p):return res
        while left + len(p) <= len(s):
            cs = Counter(s[left:left + len(p)])
            if cs == cp:
                res.append(left)
            left +=1
        return res


#######
print(Solution().findAnagrams(s = 'cbaebabacd', p = 'abc'))