class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        hash = defaultdict(int)
        for c in t:
            hash[c] += 1
        print(hash)
        left = 0
        right = 0
        min_len = float('inf')
        counter = len(t)
        res = ''
        for right,c in enumerate(s):
            right += 1
            if hash[c] > 0:
                counter -= 1
            hash[c] -= 1
            while counter == 0:
                if min_len > right - left:
                    min_len = right - left
                    res = s[left:right]
                if hash[s[left]] == 0:
                    counter += 1
                hash[s[left]] += 1
                left += 1
        return res
        
#######
print(Solution().minWindow(s ='ADOBECODEBANC',t = 'ABC'))
