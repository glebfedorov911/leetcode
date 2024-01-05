class Solution: #Time Limit
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
           return 0

        mx = 1
        for i in range(len(s)):
            d = ''
            cnt = 0
            for j in range(i, len(s)):
                if s[j] in d:
                    mx = max(mx, cnt)
                    cnt = 0
                    d = ''
                else:
                    d += s[j]
                    cnt += 1

            mx = max(mx, cnt)

        return mx

s = Solution()

print(s.lengthOfLongestSubstring("au"))