'''
    归并排序
    步骤：
        1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
        2.设定两个指针，最初位置分别为两个已经排序序列的起始位置；
        3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
        4.重复步骤3知道某一指针达到序列尾；
        5.将另一序列剩下的所有元素直接复制到合并序列尾。
'''

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    return res

arr = [17, 3, 2, 7, 5, 15, 4, 9, 8]
arr_sort = mergeSort(arr)
print(arr_sort)