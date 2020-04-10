class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complementMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[complement] = i
        return 0
    
    # #O(n^2) brute force
    # def twoSum(self, nums, target):
        # for i in range(len(nums)):
            # for j in range(i+1, len(nums)):
                # sum = nums[i] + nums[j]
                # if (sum == target):
                    # return [i, j]
        # return []
    
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))