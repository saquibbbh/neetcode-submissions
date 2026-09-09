class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in range(0, len(nums)):
            if nums[i] in hash_map:
                return True
            hash_map[nums[i]] = True
        return False