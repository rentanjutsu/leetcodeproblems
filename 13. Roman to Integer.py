class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom_num = {'I': 1,
                   'IV': 4,
                   'V': 5,
                   'IX': 9,
                   'X': 10,
                   'XL': 40,
                   'L': 50,
                   'C': 100,
                   'CD': 500,
                   'D': 500,
                   'CM': 900,
                   'M': 1000}

        str_list = []
        str_list.append(s)
        sum_list = []

        for i in str_list[::-1]:
            next = sum_list[i::-1]
            if i == 'I':
                sum_list.append['I']
            if i == 'V':
