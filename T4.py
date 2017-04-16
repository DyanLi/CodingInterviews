#!/usr/bin/env python3

'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace1(self, s):
        # write code here
        if type(s) != str:
            return False
        return s.replace(' ', '%20')

    def replaceSpace2(self, s):
        # 创建新的字符串进行替换
        temp_str = ''
        if type(s) != str:
            return
        for c in s:
            if c == ' ':
                temp_str += '%20'
            else:
                temp_str += c
        return temp_str


s = 'we are happy'
test = Solution()
print(test.replaceSpace1(s))
print(test.replaceSpace2(s))

