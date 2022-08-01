class Solution(object):
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        queue = deque()
        res = []
        max_num = float('-inf')
        if k == 1:
            return nums
        for i in range(len(nums)):

            while len(queue) >= k:
                if max_num == nums[queue[0]]:
                    max_num = float('-inf')
                queue.popleft()
            queue.append(i)
            max_num = max(max_num,nums[i])
            
            if len(queue) == k:
                print(queue)
                print(max_num)
                res.append(max_num)
        return res



######
# print(Solution().maxSlidingWindow(nums = [1,-1], k = 1))
print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
