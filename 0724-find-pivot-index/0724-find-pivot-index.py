class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Sum=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            right_sum=Sum-left_sum-nums[i]
            if (left_sum==right_sum):
                return i
            left_sum+=nums[i]
        return -1

        