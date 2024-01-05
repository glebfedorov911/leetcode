class Solution: #Time Limit
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
           return 0

        checklist = {}
        st = 0
        leng = 0
        for i, v in enumerate(s):
            if v in checklist:
                st = max(st, checklist[v] + 1)
            checklist[v] = i
            leng = max(leng, i - st + 1)

        return leng

s = Solution()

print(s.lengthOfLongestSubstring("au"))