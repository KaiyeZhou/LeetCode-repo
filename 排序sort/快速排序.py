'''
    快速排序
    --快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）
    --快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 记号中隐含的常数因子很小，
      比复杂度稳定等于 O(nlogn) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
    1. 从数列中挑出一个元素，称为 “基准”（pivot）;
    2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，
       该基准就处于数列的中间位置。这个称为分区（partition）操作；
    3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
'''

# 第一种
def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# 第二种
def quickSort_2(arr):
    if arr == []:
        return []
    else:
        pivot = arr[0]
        arr_min = quickSort_2([l for l in arr[1:] if l < pivot])
        arr_max = quickSort_2([m for m in arr[1:] if m >= pivot])
        return arr_min + [pivot] + arr_max


# 第三种
def qucikSort_3(arr, left, right):
    if left >= right:
        return arr
    key = arr[left]
    low = left
    high = right
    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]
    arr[right] = key
    qucikSort_3(arr, low, left - 1)
    qucikSort_3(arr, left + 1, high)
    return arr



arr = [17, 3, 2, 7, 5, 15, 4, 9, 8]
# arr = [49, 38, 65, 97, 76, 13, 27, 49]
# arr_sort = quickSort(arr)
arr_sort = quickSort_2(arr)
# arr_sort = qucikSort_3(arr, 0, len(arr) - 1)
print(arr_sort)
