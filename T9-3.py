#!/usr/bin/env python3

'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''


class Solution:
    def rectCover(self, number):
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

test = Solution()
print(test.rectCover(3))
