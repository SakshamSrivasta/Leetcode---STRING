class Solution(object):
    def reportSpam(self, message, bannedWords):
        """
        :type message: List[str]
        :type bannedWords: List[str]
        :rtype: bool
        """
        count=0
        s=set(bannedWords)
        for word in message:
            if word in s:
                count+=1
            if count>=2:
                return True
        return False
        