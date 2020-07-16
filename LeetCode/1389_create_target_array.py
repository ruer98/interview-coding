class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target
        
 if __name__ == '__main__':
    print('actual:  ', str(Solution().createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
    print('expected: [0, 4, 1, 3, 2]')