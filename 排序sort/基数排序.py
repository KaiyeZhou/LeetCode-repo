'''
基数排序：通过序列中各个元素的值，对排序的N个元素进行若干趟的“分配”与“收集”来实现排序。
分配：我们将L[i]中的元素取出，首先确定其个位上的数字，根据该数字分配到与之序号相同的桶中
收集：当序列中所有的元素都分配到对应的桶中，再按照顺序依次将桶中的元素收集形成新的一个待排序列L[ ]
对新形成的序列L[]重复执行分配和收集元素中的十位、百位...直到分配完该序列中的最高位，则排序结束
'''

def radix_sort(arr):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(arr):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(arr)):
            num = (arr[i] // 10 ** digit) % 10
            bucket[num].append(arr[i])
        arr.clear()
        for i in range(len(bucket)):
            arr += bucket[i]
        digit += 1
    return arr

arr = [17, 3, 2, 7, 5, 15, 4, 9, 8]
arr_sort = radix_sort(arr)
print(arr_sort)