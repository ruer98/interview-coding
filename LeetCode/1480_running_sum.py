# 1480: Running Sum of 1d Array
"""
Given an array nums. We define a running sum of an array as 
runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""
class Solution:
    def runningSum(self, nums):
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum
        return nums
    
    def runningSum2(self, nums):
        sum = 0
        sum_list = []
        for num in nums:
            sum += num
            sum_list.append(sum)
        return sum_list

if __name__ == '__main__':
    print(Solution().runningSum([1,2,3,4]))