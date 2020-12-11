import random
from time import time

def get_rows(matrix):
	return len(matrix)

def get_columns(matrix):
	return len(matrix[0])

def print_matr(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print(matrix[i][j], end = ' ')
		print()

def default_mult(matrix1, matrix2):
	if get_columns(matrix1) != get_rows(matrix2):
		print('Error')
		return

	result = [[0 for j in range(get_rows(matrix1))] for i in range(get_columns(matrix2))]

	for i in range(len(matrix1)):
		for j in range(len(matrix2[0])):
			for k in range(len(matrix1[0])):
				result[i][j] += matrix1[i][k] * matrix2[k][j]
	return result

def winograd_multiply(matrix1, matrix2):
	if get_columns(matrix1) != get_rows(matrix2):
		print('Error')
		return

	result = [[0 for j in range(get_rows(matrix1))] for i in range(get_columns(matrix2))]

	mulH = [0 for i in range(get_rows(matrix1))]
	for i in range(get_rows(matrix1)):
		for j in range(int(get_columns(matrix1) / 2)):
			mulH[i] += matrix1[i][j * 2] * matrix1[i][j * 2 + 1]

	mulV = [0 for i in range(get_columns(matrix2))]
	for i in range(get_columns(matrix2)):
		for j in range(int(get_columns(matrix1) / 2)):
			mulV[i] += matrix2[j * 2][i] * matrix2[j * 2 + 1][i]

	for i in range(get_rows(matrix1)):
		for j in range(get_columns(matrix2)):
			result[i][j] = -mulH[i] - mulV[j]
			for k in range(int(get_columns(matrix1) / 2)):
				result[i][j] += (matrix1[i][2 * k] + matrix2[2 * k + 1][j]) * (matrix1[i][2 * k + 1] + matrix2[2 * k][j])

	if get_columns(matrix1) % 2 == 1:
		for i in range(get_rows(matrix1)):
			for j in range(get_columns(matrix2)):
				result[i][j] += matrix1[i][get_columns(matrix1) - 1] * matrix2[get_columns(matrix1) - 1][j]

	return result

def improved_winograd_multiply(matrix1, matrix2):
	if get_columns(matrix1) != get_rows(matrix2):
		print('Error')
		return

	result = [[0 for j in range(get_rows(matrix1))] for i in range(get_columns(matrix2))]
	mulH = [0 for i in range(get_rows(matrix1))]
	mulV = [0 for i in range(get_columns(matrix2))]

	for i in range(get_rows(matrix1)):
		for j in range(0, get_columns(matrix1) - get_columns(matrix1) % 2, 2):
			mulH[i] += matrix1[i][j] * matrix1[i][j + 1]

	for i in range(get_columns(matrix2)):
		for j in range(0, get_rows(matrix2) - get_rows(matrix2) % 2, 2):
			mulV[i] += matrix2[j][i] * matrix2[j + 1][i]

	for i in range(get_rows(matrix1)):
		for j in range(get_columns(matrix2)):
			buff = -mulH[i] - mulV[j]
			for k in range(0, get_columns(matrix1) - get_columns(matrix1) % 2, 2):
				buff += (matrix1[i][k + 1] + matrix2[k][j]) * (matrix1[i][k] + matrix2[k + 1][j])
			result[i][j] = buff

	if get_columns(matrix1) % 2:
		for i in range(get_rows(matrix1)):
			for j in range(get_columns(matrix2)):
				result[i][j] += matrix1[i][get_columns(matrix1) - 1] * matrix2[get_columns(matrix1) - 1][j]

	return result

matrix1 = [ [1, 2, 3],
			[2, 6, 8] ]

matrix2 = [ [1, 8],
			[5, 6],
			[9, 8] ]

def matrix_test():
	M = random.randint(1, 30)
	N = random.randint(1, 30)
	Q = random.randint(1, 30)

	matrix1 = [[random.randint(1, 100) for j in range(M)] for i in range(N)]
	matrix2 = [[random.randint(1, 100) for j in range(N)] for i in range(Q)]

	res1 = default_mult(matrix1, matrix2)
	res2 = winograd_multiply(matrix1, matrix2)
	res3 = improved_winograd_multiply(matrix1, matrix2)

	return res1 == res2 == res3


def time_analysis_even(n_iter):
	for i in range(100, 501, 100):
		print(i)
		matrix1 = [[random.randint(1, 100) for j in range(i)] for k in range(i)]
		matrix2 = [[random.randint(1, 100) for j in range(i)] for k in range(i)]
		t1 = time()
		for j in range(n_iter):
			res = default_mult(matrix1, matrix2)
		t2 = time()
		print('Default multiply: ' + str((t2 - t1) / n_iter))
		t1 = time()
		for j in range(n_iter):
			res = winograd_multiply(matrix1, matrix2)
		t2 = time()
		print('Winograd multiply: ' + str((t2 - t1) / n_iter))
		t1 = time()
		for j in range(n_iter):
			res = improved_winograd_multiply(matrix1, matrix2)
		t2 = time()
		print('Improved winograd multiply: ' + str((t2 - t1) / n_iter))

def time_analysis_odd(n_iter):
	for i in range(101, 502, 100):
		print(i)
		matrix1 = [[random.randint(1, 100) for j in range(i)] for k in range(i)]
		matrix2 = [[random.randint(1, 100) for j in range(i)] for k in range(i)]
		t1 = time()
		for j in range(n_iter):
			res = default_mult(matrix1, matrix2)
		t2 = time()
		print('Default multiply: ' + str((t2 - t1) / n_iter))
		t1 = time()
		for j in range(n_iter):
			res = winograd_multiply(matrix1, matrix2)
		t2 = time()
		print('Winograd multiply: ' + str((t2 - t1) / n_iter))
		t1 = time()
		for j in range(n_iter):
			res = improved_winograd_multiply(matrix1, matrix2)
		t2 = time()
		print('Improved winograd multiply: ' + str((t2 - t1) / n_iter))


matrix1 = [[random.randint(1, 100) for j in range(10)] for k in range(10)]
print("EVEN")
time_analysis_even(10) 
print("ODD")
time_analysis_odd(10)
