# Time Complexity = O(n)
# Space Complexity = O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        max_area = 0
        while low < high:
            area = min(height[low], height[high]) * (high - low)

            if area > max_area:
                max_area = area

            if height[low] > height[high]:
                high -= 1

            else:
                low += 1
        return max_area
        