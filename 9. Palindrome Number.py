class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev_list = []
        val = str(int(x))

        for i in val:
            rev_list.append(i)

        ver = rev_list[::-1]

        if rev_list == ver:
            return True
        else:
            return False
