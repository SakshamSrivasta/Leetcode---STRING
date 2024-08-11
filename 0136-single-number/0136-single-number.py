class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for x in nums:
            if x in count:
                count[x]+=1
            else:
                count[x]=1
        for x in count:
            if count[x]==1:
                return x
                break

        