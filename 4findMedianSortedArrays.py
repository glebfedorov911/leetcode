from math import floor, ceil
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = self.quick_sort(nums1 + nums2)
        if len(n) % 2 != 0:
            return n[len(n) // 2]
        else:
            b, s = int(len(n)/2), int(len(n)/2-1)
            return (n[b]+n[s]) / 2

    def quick_sort(self, array: List[int]) -> List[int]:
        less, equal, greater = [], [], []

        if len(array) <= 1:
            return array
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)

        return self.quick_sort(less) + equal + self.quick_sort(greater)

s = Solution()
print(s.findMedianSortedArrays(nums1 = [1], nums2 = [2, 3]))