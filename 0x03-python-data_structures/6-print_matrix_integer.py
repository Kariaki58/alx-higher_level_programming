def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[i])):
                print("{}".format(matrix[i][j]), end="")
                if j < len(matrix[i]) - 1:
                    print(end=" ")
        print()
