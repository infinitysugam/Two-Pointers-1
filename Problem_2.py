# For this we loop for each element and solve the rest using 2 sum problem
# Time complexity = O(n2)
# Space Complexity = O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        output_array = []
        for i in range(0,len(nums)):
            if i!=0 and nums[i]== nums[i-1]:
                continue
            low = i+1
            high = len(nums)-1

            while low<high:
                sum = nums[i] + nums[low] + nums[high]
                if sum > 0 :
                    high = high -1
                elif sum < 0:
                    low = low + 1
                else:
                    output_array.append([nums[i],nums[low],nums[high]])
                    low = low +1 
                    high = high - 1
                    while low<high and nums[low] == nums[low-1]:
                        low = low + 1
                    while low<high and nums[high] == nums[high+1]:
                        high = high -1
        
        return output_array

        