class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)
        if (y[0] == '-'):
            return y[0] + y[::-1]
        else:
            return y[::-1]
            
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123456))