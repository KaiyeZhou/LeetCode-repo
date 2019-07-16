'''
    堆排序
    --堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
      堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：
    1.大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
    2.小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；
    堆排序的平均时间复杂度为 Ο(nlogn)。
    步骤：
        1. 创建一个堆 H[0……n-1]；
        2. 把堆首（最大值）和堆尾互换；
        3. 把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；
        3. 重复步骤 2，直到堆的尺寸为 1。    
'''

# 调整堆
def adjust_heap(arr, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    maxIndex = i
    if i < size // 2:    #判断是否存在子节点
        if lchild < size and arr[lchild] > arr[maxIndex]:
            maxIndex = lchild
        if rchild < size and arr[rchild] > arr[maxIndex]:
            maxIndex = rchild
        if maxIndex != i:
            arr[maxIndex], arr[i] = arr[i], arr[maxIndex]
            adjust_heap(arr, maxIndex, size)

# 创建堆
def build_heap(arr, size):
    for i in range((size // 2) - 1, -1, -1):
        adjust_heap(arr, i, size)

# 堆排序
def heap_sort(arr):
    size = len(arr)
    build_heap(arr, size)
    for i in range(size - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        adjust_heap(arr, 0, i)    # 最后一个数不参与接下来的排序了，相当于从二叉树中抹去

arr = [17, 3, 2, 7, 5, 15, 4, 9, 8]
heap_sort(arr)
print(arr)