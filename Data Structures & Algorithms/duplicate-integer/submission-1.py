class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for i in nums:
            if i in unique:
                return True
            unique.append(i)
        return False

        