import random
import matplotlib.pyplot as plt
import numpy as np

#рандомное заполнение
def rand(length):
    result = []

    for i in range(length):
        result.append([])
        for j in range(length):
            a = random.randint(1, 30)
            result[-1].append(a)
    return result

#рандомное удаление
def rand_delete(array, value):
    delete_x = []
    delete_y = []
    for i in range(10):
        while True:
            x = random.randint(0, len(array) - 1)
            y = random.randint(0, len(array) - 1)
            if array[y][x] != value: break
        delete_x.append(len(array) * y + x)
        delete_y.append(array[y][x])
        array[y][x] = value
    return (delete_x, delete_y)

#восстановление путем линейной аппроксимации
def recovery_points(array):
    transform(array)
    new = []
    delete_x, delete_y = rand_delete(array, None)
    new_x = []
    new_y = []
    plt.scatter(delete_x, delete_y, color="red")
    for i in array: new += i
    n = len(new)
    
    index = 0
    start_index = 0
    finish_index = 0
    while index < n:
        while index < n and new[index] == None:
            finish_index += 1
            index += 1
        if start_index != finish_index:
            recover(new, start_index, finish_index, new_x, new_y)
        index += 1
        finish_index = index
        start_index = index


    plt.scatter(new_x, new_y, color="green", marker="^", s = 100)
    plt.show()
    return new

def recover(array, start, finish, x, y):
    k = 0
    b = 0
    if finish == len(array): finish -= 1
    if array[finish] == None: 
        k = array[start - 1] - array[start - 2]
        b = array[start - 1] - k * (start - 1)

    elif array[start] == None:
        if start == 0:
            k = array[finish] / finish
            b = array[finish] - k * finish
        else:
            k = (array[start - 1] - array[finish]) / (finish - start)
            b = array[start - 1] - k * (start - 1)

        for i in range(start, finish):
            array[i] = k * i + b
            x.append(i) 
            y.append(array[i])

#восстановление путем корреляции
def correlation(array):
    print("YOUR MATRIX: \n")
    rand_delete(array, 0)
    Print(array)
    print("\n")
    data = []
    while len(array) > 0:
        data.append([array.pop(), []])

    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
               a = np.array(data[i][0])
               b = np.array(data[j][0])
               if sum(data[j][0]) == 0: data[i][1].append([0, j])
               else: data[i][1].append([np.corrcoef(a, b).min(), j])
        data[i][1].sort()

    while full_recover(data):
        for i in data: recover_correlation(i, data)
    for i in range(len(data)):  data[i] = data[i][0]
    return data

def recover_correlation(row, data):
    deleten = []
    for i in range(len(row[0])):
        if row[0][i] == 0: deleten.append(i)

    for i in range(len(row[1])):
        for j in range(len(deleten)):
            if deleten[j] == None: continue
            row_index = row[1][i][1]
            element = data[row_index][0][deleten[j]]
            if element != 0:
                row[0][deleten[j]] = data[row[1][i][1]][0][deleten[j]]
                deleten[j] = None

def full_recover(data):
    for row in data:
        if 0 in row[0]: return True
    return False

#соединение отрезков
def segments(x_1, x_2, y_1, y_2):
    for i in range(len(x_2)):
        for x in range(len(x_1)):
            if x_1[x] == x_2[i]: plt.plot([x_1[x], x_1[x]], [y_2[i], y_1[x]], color = "red", linewidth = 1)

#трансформация данных
def transform(array):
    x = []
    y = []
    n = len(array)
    for i in range(n * n):
        x.append(i)
    for i in array:
        y += i
    plt.scatter(x, y, s = 5)

#красивый вывод
def Print(data):
    col_width = max(word for row in data for word in row)
    for row in data:
       print(" ".join(str(word).ljust(len(str(col_width))) for word in row))
    
#для кореляции необходима матрица размером не меньше 11 так как чисто гипотетически во всех рядах может быть уничтожен 1  и тот же элемент
#и восстановить его будет невозможно
Print(correlation(rand(11)))
recovery_points(rand(20))