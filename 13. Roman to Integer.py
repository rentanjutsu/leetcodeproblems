class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom_num = {'I': 1,
                   'IV': 3,
                   'V': 5,
                   'IX': 8,
                   'X': 10,
                   'XL': 30,
                   'L': 50,
                   'XC': 80,
                   'C': 100,
                   'CD': 300,
                   'D': 500,
                   'CM': 800,
                   'M': 1000}
        str_list = s[::-1]
        sum_list = []

        for i in range(len(str_list)):
            current = str_list[i]
            if i + 1 < len(str_list):
                nxt = str_list[i + 1]
            else:
                nxt = ''
            if current == 'I':
                sum_list.append(rom_num['I'])
            if current == 'V':
                if nxt == 'I':
                    sum_list.append(rom_num['IV'])
                else:
                    sum_list.append(rom_num['V'])
            if current == 'X':
                if nxt == 'I':
                    sum_list.append(rom_num['IX'])
                else:
                    sum_list.append(rom_num['X'])
            if current == 'L':
                if nxt == 'X':
                    sum_list.append(rom_num['XL'])
                else:
                    sum_list.append(rom_num['L'])
            if current == 'C':
                if nxt == 'X':
                    sum_list.append(rom_num['XC'])
                else:
                    sum_list.append(rom_num['C'])
            if current == 'D':
                if nxt == 'C':
                    sum_list.append(rom_num['CD'])
                else:
                    sum_list.append(rom_num['D'])
            if current == 'M':
                if nxt == 'C':
                    sum_list.append(rom_num['CM'])
                else:
                    sum_list.append(rom_num['M'])
        return sum(sum_list)