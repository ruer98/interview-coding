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
        return -1
    
    # #O(n^2) brute force
    # def twoSum(self, nums, target):
        # for i in range(len(nums)):
            # for j in range(i+1, len(nums)):
                # sum = nums[i] + nums[j]
                # if (sum == target):
                    # return [i, j]
        # return []
        
    # Hashing solution 1
    # def twoSum(self, nums, target):
        # has_nums = {}
        # for index, num in enumerate(nums):
            # try:
                # hash_nums[num].append(index)
            # except KeyError:
                # hash_nums[num] = [index]
        # for index, num in enumerate(nums):
            # another = target - num
            # try:
                # candidate = hash_nums[another]
                # if (another == num):
                    # if len(candidate) > 1:
                        # return candidate
                    # else:
                        # continue
                # else:
                    # return [index, candidate[0]]
            # except KeyError:
                # pass
    
    # Hashing solution 2
    # def twoSum(self, nums, target):
        # hash_nums = {}
        # for index, num in enumerate(nums):
            # another = target - num
            # try:
                # hash_nums[another]
                # return [hash_nums[another], index]
            # except KeyError:
                # hash_nums[num] = index
                
    # Two point
    # def twoSum(self, nums, target):
        # nums_index = [(v, index) for index, v in enumerate(nums)]
        # nums_index.sort()
        # begin, end = 0, len(nums) - 1
        # while begin < end:
            # curr = nums_index[begin][0] + nums_index[end][0]
            # if curr == target:
                # return [nums_index[begin][1], nums_index[end][1]]
            # elif curr < target:
                # begin += 1
            # else:
                # end -= 1
                
                
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))