class Solution:
    def isValid(self, s):
        #constraints
        if len(s) <= 1 or len(s) >= 10**4:
            return False
        
        stack=[]
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if not stack or {')':'(',']':'[','}':'{'}[i] != stack[-1]:
                    return False
                stack.pop()
        return not stack
    
if __name__ == '__main__':
    print('[]{()}')
    print('actual:  ', str(Solution().isValid('[]{()}')))
    print('expected: True')
    print('{{}')
    print('actual:  ', str(Solution().isValid('{{}')))
    print('expected: False')
    