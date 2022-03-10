#суммирование/вычитание матриц
def matrix_sum(matrix_1, matrix_2, operation):
    znak = 0
    result = []

    if operation == "+": znak = 1
    else: znak = -1

    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        print("Error, unpossible sum those matrixs :(")
        return
    else:
        for i in range(len(matrix_1)):
            result.append([])
            for j in range(len(matrix_1[0])):
                result[i].append(matrix_1[i][j] + matrix_2[i][j] * znak)

    return result

#транспонирование матриц
def rotate(matrix):
    new = []
    while len(matrix[0]) > 0:
        new.append(list(map(lambda x: x.pop(), matrix)))
    new.reverse()
    return new

#красивый вывод
def Print(data):
    col_width = max(word for row in data for word in row)
    for row in data:
       print(" ".join(str(word).ljust(len(str(col_width))) for word in row))

#квадрат матрицы(Штрайссен)
def square_matrix(matrix_A, matrix_B):

    if len(matrix_A) <= 100:
        return square_matrix_2(matrix_A, matrix_B)

    if len(matrix_A) % 2 != 0:
        matrix_A = list(map(lambda x: x + [0], matrix_A))
        matrix_A.append([0] * len(matrix_A[0]))

        matrix_B = list(map(lambda x: x + [0], matrix_B))
        matrix_B.append([0] * len(matrix_B[0]))


    partA_1, partA_2, partA_3, partA_4 = split_matrix(matrix_A)
    partB_1, partB_2, partB_3, partB_4 = split_matrix(matrix_B)

    #сам алгоритм
    S1 = matrix_sum(partB_2, partB_4, "-")
    S2 = matrix_sum(partA_1, partA_2, "+")
    S3 = matrix_sum(partA_3, partA_4, "+")
    S4 = matrix_sum(partB_3, partB_1, "-")
    S5 = matrix_sum(partA_1, partA_4, "+")
    S6 = matrix_sum(partB_1, partB_4, "+")
    S7 = matrix_sum(partA_2, partA_4, "-")
    S8 = matrix_sum(partB_3, partB_4, "+")
    S9 = matrix_sum(partA_1, partA_3, "-")
    S10 = matrix_sum(partB_1, partB_2, "+")

    P1 = square_matrix(partA_1, S1)
    P2 = square_matrix(S2, partB_4)
    P3 = square_matrix(S3, partB_1)
    P4 = square_matrix(partA_4, S4)
    P5 = square_matrix(S5, S6)
    P6 = square_matrix(S7, S8)
    P7 = square_matrix(S9, S10)

    C1 = matrix_sum(matrix_sum(matrix_sum(P5, P4, "+"), P2, "-"), P6, "+")
    C2 = matrix_sum(P1, P2, "+")
    C3 = matrix_sum(P3, P4, "+")
    C4 = matrix_sum(matrix_sum(matrix_sum(P5, P1, "+"), P3, "-"), P7, "-")

    return connect_matrix(C1, C2, C3, C4)

def split_matrix(matrix):
    part_1 = []
    part_2 = []
    part_3 = []
    part_4 = []

    middle = len(matrix) // 2

    for i in range(middle):
        part_1.append(matrix[i][:middle])
        part_2.append(matrix[i][middle:])
        part_3.append(matrix[i + middle][:middle])
        part_4.append(matrix[i + middle][middle:])

    return (part_1, part_2, part_3, part_4)

def connect_matrix(C1, C2, C3, C4):
    A = []
    B = []
    for i in range(len(C1)):
        A.append(C1[i] + C2[i])
        B.append(C3[i] + C4[i])

    return A + B

def delete_zero(matrix):
    i = 0
    while i < len(matrix):
        if sum(matrix[i]) == 0:
            matrix.pop(i)
            i -= 1
        i += 1

    i = 0
    while i < len(matrix[0]):
        summ = 0
        j = 0
        while j < len(matrix):
            summ += matrix[j][i]
            j += 1
        if summ == 0:
            for a in matrix:
                a.pop(i)
            i -= 1
        i += 1

    return matrix

def square_matrix_2(matrix_A, matrix_B):
    answer = []
    for i in matrix_A:
        row = []
        for j in range(len(i)):
            result = 0
            for k in range(len(i)): result += i[k] * matrix_B[k][j]
            row.append(result)
        answer.append(row)

    return answer
                

#определитель матрицы
def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    if len(matrix) == 1:
        return matrix[0][0]
    result = 0
    new = []
    for i in range(len(matrix[0])):
        for arr in matrix[1:]:
            arr = arr[:]
            arr.pop(i)
            new.append(arr)
        result += (-1) ** (i % 2) * determinant(new) * matrix[0][i]
        new = []
    return result
