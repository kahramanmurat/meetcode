class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        pre_prefix = 1
        for i in range(len(nums)):
            res[i] = pre_prefix
            pre_prefix *= nums[i]
        post_prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post_prefix
            post_prefix *= nums[i]
        return res
