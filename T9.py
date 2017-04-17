#!/usr/bin/env python3

'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

class Solution:
    def Fibonacci(self, n=39):
        # write code here
        fib1 = 0
        fib2 = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2,n+1):
            fibN = fib1 + fib2
            fib1 = fib2
            fib2 = fibN
        return fibN

test = Solution()
print(test.Fibonacci(3))