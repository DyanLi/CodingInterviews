#!/usr/bin/env python3
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法.
'''

class Solution:
    def jumpFloorII(self, number):
        fib = [1,1,]
        if number == 0:
            return 0
        if number == 1:
            return 1
        for i in range(2, number + 1):
            fib.append(sum(fib))
        return fib[number]

test = Solution()
print(test.jumpFloorII(4))