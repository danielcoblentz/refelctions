# implementation of binary search

def binarySearch(arr: list[int], target: int) -> int:
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    print(binarySearch([1, 3, 3, 4, 5, 6, 7, 8], 8 )) # returns the index position of target