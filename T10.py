#!/usr/bin/env python3

'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
    # python not just use 32 bit to present a int type
    # some method in book cant be used in python
    def NumberOf1(self, n):
        return sum([(n>>i)&1 for i in range(0,32)])

    def NumberOf2(self, n):
        cnt = 0
        flag = 1
        for i in range(32):
            if (n & flag):
                cnt += 1
            flag = flag << 1
        return cnt




test = Solution()
print(test.NumberOf1(-3))
print(test.NumberOf2(-3))