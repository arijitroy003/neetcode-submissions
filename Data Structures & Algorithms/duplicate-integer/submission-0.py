class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        set_nums = set(nums)
        if len(set_nums) == n:
            return False
        else:
            return True