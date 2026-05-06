class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)

        for i in range(len(nums)):
            if nums[i] in n:
                n.remove(nums[i])
            else:
                return True
        return False