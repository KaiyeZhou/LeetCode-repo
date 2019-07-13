'''
    希尔排序
    基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
    步骤：1. 选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
         2. 按增量序列个数 k，对序列进行 k 趟排序；
         3.每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
'''

def shellSort(arr):
    gap = len(arr)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(arr)):
            for j in range(i % gap, i, gap):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr

def shellSort_2(arr):
    gap = 1
    while gap < len(arr) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = gap // 3
    return arr



arr = [17, 3, 2, 7, 5, 15, 4, 9, 8]
# arr_sort = shellSort(arr)
arr_sort = shellSort_2(arr)
print(arr_sort)