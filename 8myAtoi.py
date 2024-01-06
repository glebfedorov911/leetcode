import string


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if len(s) <= 0:
            return 0

        MAX = 2**31-1
        MIN = -2**31

        every_element_split = [i for i in s]

        is_neg = False
        if every_element_split[0] == '-':
            is_neg = True
            every_element_split = every_element_split[1:]
        elif every_element_split[0] == '+':
            every_element_split = every_element_split[1:]
        elif every_element_split[0] in string.ascii_letters:
            return 0

        every_element_split = [every_element_split[i] if every_element_split[i] in '0123456789' else 'STOP' for i in range(len(every_element_split))]
        if 'STOP' in every_element_split:
            every_element_split = every_element_split[:every_element_split.index('STOP')]

        num = ''.join(every_element_split)
        if is_neg:
            num = '-' + ''.join(every_element_split)

        if not num:
            return 0

        try:
            num = int(num)
        except:
            return 0


        if MAX < num:
            return MAX
        if MIN > num:
            return MIN

        return num

s = Solution()
print(s.myAtoi(' '))