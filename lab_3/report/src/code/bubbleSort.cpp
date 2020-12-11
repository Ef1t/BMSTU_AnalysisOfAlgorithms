def bubble_sort(arr):
    if len(arr) <= 1:
        return

    for i in range(len(arr)):
        flag = 0;
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                flag = 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if flag == 0:
            break

    return arr