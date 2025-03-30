# We use three pointers and swap according to the logic
# Time Complexity = O(n)
# Space Complexity = O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low = 0 
        mid = 0 
        high = len(nums)-1

        while mid<=high:
            if nums[mid]==2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high = high -1
            elif nums[mid] == 0 :
                nums[low],nums[mid] = nums[mid],nums[low]
                low = low + 1
                mid = mid +1
            else:
                mid = mid + 1
            