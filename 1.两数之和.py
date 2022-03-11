class Solution:
    def twoSum(self, nums,target):
        hash_map = {}
        for index, value in enumerate(nums):
            remain = target - value
            if remain in hash_map:
                return [hash_map[remain],index]
            else:
                hash_map[value] = index

#######
print(Solution().twoSum([2,7,11,15],9))
