class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x
        sum = 0
        sign = 1
        if num < 0:
            sign = -1
            num = abs(num)
        while num > 0:
            rem = num % 10
            sum = sum * 10 + rem
            num = num // 10
        if not -2147483648 < sum < 2147483648:
            return 0
        return sign * sum
