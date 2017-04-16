#!/usr/bin/env python3

'''
输入一个链表，从尾到头打印链表每个节点的值。
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        # return value
        self.next = None

class testolution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode.val == None :
            return False
        l = []
        head = listNode
        while head:
            l.append(head.val)
            head = head.next
        l.reverse()
        return l


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(12)
node1.next = node2
node2.next = node3

node4 = ListNode(13)

node5 = ListNode()

test = testolution()
print(test.printListFromTailToHead(node1))
print(test.printListFromTailToHead(node4))
print(test.printListFromTailToHead(node5))

