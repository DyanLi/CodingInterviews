#!/usr/bin/env python3

'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

class Solution:
    def jumpFloor(self, number):
        # write code here
        fib1 = 1
        fib2 = 1
        if number == 0:
            return 0
        if number == 1:
            return 1
        for i in range(2, number + 1):
            fibN = fib1 + fib2
            fib1 = fib2
            fib2 = fibN
        return fibN