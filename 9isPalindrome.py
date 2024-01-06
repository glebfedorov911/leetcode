class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x) == 0 or len(x) == 1:
            return True
        else:
            return x == x[::-1]
        return self.isPalindrome(x[1:len(x)-1])

s = Solution()
print(s.isPalindrome(-121))