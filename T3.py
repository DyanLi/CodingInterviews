#!/usr/bin/env python3

'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
'''


class Solution:
    # array 二维列表
    # target 目标树

    def Find(self, target, array):
        if len(array[0]) == 0:
            return False

        rows = len(array)
        columns = len(array[0])

        # 判断非法输入
        if not (isinstance(target,float) or isinstance(target, int)):
            return False

        # 指针放在右上角
        row = 0
        column = columns -1
        while row < rows and column >= 0:
            found_num = array[row][column]
            # 判断非法输入
            if not (isinstance(found_num, float) or isinstance(found_num, int)):
                return False

            if found_num > target:
                column -= 1
            elif found_num < target:
                row += 1
            else:
                return True
        return False


array1 = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [6, 8, 11, 15]]
array2 = []
array3 = [[]]

test = Solution()
print(test.Find(1,array1))
print(test.Find(15,array1))
print(test.Find(10.0, array1))

print(test.Find('', array1))
print(test.Find(0, array1))
print(test.Find(25, array1))
print(test.Find(5, array1))

print(test.Find(11, array3))





