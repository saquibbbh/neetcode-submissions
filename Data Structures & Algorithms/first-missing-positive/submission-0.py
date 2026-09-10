class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 1

        while n in nums:
            n += 1

        return n