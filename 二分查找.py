def binary_search(alist, item):
    """二分查找递归版本"""
    """二分查找算法：必须为以排序的顺序表。先找顺序表的中间位置比较，若大于则去左边元素为新表递归，若小于则取右边元素为新表递归"""
    n = len(alist)
    mid = n // 2
    if n > 0:
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search(alist[0:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


if __name__ == "__main__":
    a = [1, 3, 4, 5, 6]
    print(binary_search(a, 4))
    print(binary_search(a, 5))
    print(binary_search(a, 8))
