class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curSum = 0
        for num in nums:
            curSum = max(curSum + num, num)
            res = max(res, curSum)
        return res

        