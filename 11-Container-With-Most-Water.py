from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxarea = max(area, maxarea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea


height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 8, 7, 8]
print(Solution.maxArea(self=height, height=height))
