from typing import  List

class Solution: #Work all
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j] if i < j else [j, i]

        return []

s = Solution()

print(s.twoSum(nums = [3,2,4], target = 6))