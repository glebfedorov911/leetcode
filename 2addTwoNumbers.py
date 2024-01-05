from typing import Optional, List

class Solution:
    def addTwoNumbers(self, l1: Optional[List], l2: Optional[List]) -> Optional[List]:
        return [i for i in str(int(''.join(list(map(str, l1)))[::-1])+int(''.join(list(map(str, l2)))[::-1]))[::-1]]

s = Solution()
print(s.addTwoNumbers([2,4,3], [5,6,4])) # with List Work