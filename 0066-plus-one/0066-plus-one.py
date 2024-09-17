class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        Str=""
        for num in digits:
            Str+=str(num)
        x=int(Str)
        x+=1
        y=[]
        for nums in str(x):
            y.append(int(nums))
        return y  