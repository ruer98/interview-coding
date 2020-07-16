class Solution:
    def shuffle(self, nums, n):
        for i in range(n-1):
            nums[i+1],nums[n] = nums[n], nums[i+1]
        nums[n], nums[n+1] = nums[n+1], nums[n]
        return nums
    
    def shuffle2(self,nums, n):
        new_list = []
        half_len = n
        for i in range(half_len):
            new_list.append(nums[i])
            new_list.append(nums[i+n])
        return new_list

if __name__ == '__main__':
    print('actual:  ', str(Solution().shuffle([2,5,1,3,4,7],3)))
    print('expected: [2, 3, 5, 4, 1, 7]')