import itertools

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        mx = 0
        ans_dict = {}
        for i in range(len(s)):
            cand = self.get_palindrome(s, i, i)

            ans_dict[len(cand)] = cand

        return ans_dict[max(ans_dict.keys())]

    @staticmethod
    def get_palindrome(s, start, end):
        while end + 1 < len(s) and s[start] == s[end+1]:
            end += 1

        while start > 0 and end + 1 < len(s) and s[start-1] == s[end+1]:
            start -= 1
            end += 1

        return s[start:end+1]

s = Solution()
print(s.longestPalindrome("aacabdkacaa"))
