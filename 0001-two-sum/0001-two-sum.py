class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in x:
                return [x[diff],i]
            x[n]=i
        return
        