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