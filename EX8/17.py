
matrix_sum = 0
for i in range(4):
    row = input(f"Enter {i+1} row: ")
    row = row.strip().split()
    row = [int(n) for n in row]
    matrix_sum += sum(row)

print("THe average of the matrix is {}".format(matrix_sum/16))