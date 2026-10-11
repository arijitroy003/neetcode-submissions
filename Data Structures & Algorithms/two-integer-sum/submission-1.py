class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            hash map of indices
            check diff of target - element exists in map or not
            if yes return index[diff], current_index
            else insert into index array
            no match -> return empty array
        """
        indices = {} # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                return [indices[diff],i]
            indices[n] = i

        # return []