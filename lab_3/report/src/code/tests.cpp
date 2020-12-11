def test():
    arr1 = [random.randint(1, 100) for i in range(100)]
    arr4 = arr3 = arr2 = arr1

    bubble_sort(arr1)
    selection_sort(arr2)
    qsort(arr3, 0, len(arr3) - 1)
    sorted(arr4)

    if arr1 == arr2 == arr3 == arr4:
        print("OK")