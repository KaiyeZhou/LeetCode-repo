'''
   选择排序
   1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
   2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
   3. 重复第二步，直到所有元素均排序完毕。
'''

def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

arr = [17, 3, 2, 7, 5, 15, 4, 9, 8]
arr_sort = selectionSort(arr)
print(arr_sort)