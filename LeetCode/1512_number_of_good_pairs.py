# 1512: Number of Good Pairs
"""
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
"""

class Solution:
    def numIdenticalPairs(self, nums):
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        pairs = 0
        for value in nums_dict.values():
            possible = value * (value-1) // 2
            pairs += possible
        
        return pairs

    def numIdenticalPairs2(self, nums):
        nums_dict = {}
        pairs = 0
        for num in nums:
            if num in nums_dict:
                pairs += nums_dict[num]
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        return pairs
    
if __name__ == '__main__':
    print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
    print('actual: 4')