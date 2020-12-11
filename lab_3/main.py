import random
from time import time

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

def selection_sort(arr):
	if len(arr) <= 1:
		return

	for i in range(len(arr) - 1):
		min_ind = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min_ind]:
				min_ind = j
		if min_ind != i:
			arr[i], arr[min_ind] = arr[min_ind], arr[i]

	return arr

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

def test():
	arr1 = [random.randint(1, 100) for i in range(100)]
	arr4 = arr3 = arr2 = arr1

	bubble_sort(arr1)
	selection_sort(arr2)
	qsort(arr3, 0, len(arr3) - 1)
	sorted(arr4)

	if arr1 == arr2 == arr3 == arr4:
		print("OK")

def time_analysis(n_iter):
	print("Sorted")
	for j in range(100, 1001, 100):
		print(j)
		arr = [random.randint(1, 100) for k in range(j)]
		sorted(arr)
		t1 = time()
		for i in range(n_iter):	
			bubble_sort(arr)
		t2 = time()
		print("Bubble sort: " + str((t2 - t1) / n_iter))
		t1 = time()
		for i in range(n_iter):	
			selection_sort(arr)
		t2 = time()
		print("Selection sort: " + str((t2 - t1) / n_iter))
		t1 = time()
		for i in range(n_iter):	
			qsort(arr, 0, len(arr) - 1)
		t2 = time()
		print("Quick sort: " + str((t2 - t1) / n_iter))

	print("Reverse sorted")
	for j in range(100, 1001, 100):
		print(j)
		arr = [random.randint(1, 100) for k in range(j)]
		sorted(arr, reverse = True)
		t1 = time()
		for i in range(n_iter):	
			bubble_sort(arr)
		t2 = time()
		print("Bubble sort: " + str((t2 - t1) / n_iter))
		t1 = time()
		for i in range(n_iter):	
			selection_sort(arr)
		t2 = time()
		print("Selection sort: " + str((t2 - t1) / n_iter))
		t1 = time()
		for i in range(n_iter):	
			qsort(arr, 0, len(arr) - 1)
		t2 = time()
		print("Quick sort: " + str((t2 - t1) / n_iter))

	print("Random sorted")
	for j in range(100, 1001, 100):
		print(j)
		arr = [random.randint(1, 100) for k in range(j)]
		
		t1 = time()
		for i in range(n_iter):	
			bubble_sort(arr)
		t2 = time()
		print("Bubble sort: " + str((t2 - t1) / n_iter))
		t1 = time()
		for i in range(n_iter):	
			selection_sort(arr)
		t2 = time()
		print("Selection sort: " + str((t2 - t1) / n_iter))
		t1 = time()
		for i in range(n_iter):	
			qsort(arr, 0, len(arr) - 1)
		t2 = time()
		print("Quick sort: " + str((t2 - t1) / n_iter))

time_analysis(10)

