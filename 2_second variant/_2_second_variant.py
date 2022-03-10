import random
import matplotlib.pyplot as plt

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
def rand_delete(array):
    for i in range(10):
        while True:
            x = random.randint(0, len(array) - 1)
            y = random.randint(0, len(array) - 1)
            if array[y][x] != None: break
        array[y][x] = None

#восстановление путем линейной аппроксимации
def recovery_points(array):
    

recovery_points(rand(25))
