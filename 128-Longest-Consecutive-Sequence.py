class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        longset = 0
        for n in nums:
            if (n - 1) not in numset:
                length = 0
                while (n + length) in numset:
                    length += 1
                longset = max(longset, length)
        return longset
