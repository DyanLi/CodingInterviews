#!/usr/bin/env python3

'''
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
'''


class Solution:
    def Power(self, base, exponent):
        result = 1
        if -0.0000001 < base <0.00000001:
            return 0

        if exponent < -0.0000001 :
            exponent = abs(exponent)
            for i in range(exponent):
                result *= base
                print(result)
            return 1/result
        elif exponent > 0.00000001 :
            for i in range(exponent):
                result *= base
            return result
        else:
            return 1

test = Solution()
print(test.Power(2,-3))

