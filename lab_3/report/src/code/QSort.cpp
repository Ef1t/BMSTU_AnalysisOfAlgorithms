def qsort(arr, left, right):
    if len(arr) <= 1:
        return 

    l, r = left, right
    pivot = arr[int((l + r) / 2)]

    while (l <= r):
        while arr[l] < pivot:
            l += 1
        while arr[r] > pivot:
            r -= 1

        if (l <= r):
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1

    if left < r:
        qsort(arr, left, r)
    if right > l:
        qsort(arr, l, right)