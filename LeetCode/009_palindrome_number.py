class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            orig_num = x
            rev_num = 0
            while x > 0:
                last_digit = x % 10
                x //= 10
                rev_num = rev_num*10 + last_digit
            return (orig_num == rev_num)
    
    """
    def strPalindrome(self, x):
        y = str(x)
        if (y == y[::-1]):
            return True
        return False
    """
    
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(123454321))    #true
    print(s.isPalindrome(12345))        #false
    print(s.isPalindrome(1))            #true
    