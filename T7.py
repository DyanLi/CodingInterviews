#!/usr/bin/env python3

'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

class Solution:
    def __init__(self):
        self.stack1 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if len(self.stack1) > 0 :
            return self.stack1.pop(0)
        else:
            return None
