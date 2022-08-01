class Solution:
    def minSubArrayLen(self, target, nums):
        sum=0
        res = float('inf')
        left = 0
        for right,num in enumerate(nums):
            right +=1
            sum += num
            while sum >= target:
                print(left,right,sum)
                if right - left < res:
                    res = right - left
                sum -= nums[left]
                left +=1
        if res == float('inf'):
            return 0
        return res

######
print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
