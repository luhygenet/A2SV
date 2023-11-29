class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0: return False

        div=1
        while div*10 <= x:
            div*=10
        while x:
            if x%10!=x//div:
                return False
            x=(x%div)//10
            div=div/100
        return True 