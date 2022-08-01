class Solution:
    def lengthOfLongestSubstring(self, s):
        from collections import defaultdict
        hash = defaultdict(int)
        left = 0
        max_len = 0
        counter = 0
        for right,c in enumerate(s):
            right +=1
            if hash[c] > 0:
                counter += 1
            hash[c] += 1
            while counter > 0:
                if hash[s[left]] > 1:
                    counter -= 1
                hash[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len

######
print(Solution().lengthOfLongestSubstring('baa'))