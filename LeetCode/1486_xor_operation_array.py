class Solution:
    def xorOperation(self, n, start):
        nums = [None] * n
        xor = 0
        for i in range(n):
            nums[i] = start + 2*i
            xor ^= nums[i]
        return xor
        
if __name__ == '__main__':
    print('actual:  ', str(Solution().xorOperation([],3)))
    print('expected: [2, 3, 5, 4, 1, 7]')