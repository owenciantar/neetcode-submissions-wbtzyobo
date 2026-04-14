class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        max_consecutive = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                consecutive += 1
            else:
                if consecutive > max_consecutive:
                    max_consecutive = consecutive
                consecutive = 0
        if consecutive > max_consecutive:
            max_consecutive = consecutive
        return max_consecutive