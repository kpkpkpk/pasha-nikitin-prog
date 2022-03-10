import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time
from module1 import *

#рандомизированное заполнение
def rand(length):
    result = []

    for i in range(length):
        result.append([])
        for j in range(length):
            a = random.randint(50, 100)
            result[-1].append(a)
    return result

#герератор матриц
def matrix_generator(size, step):
    for i in range(1, size, step):
        yield rand(i)

#улучшение
def develop():
    fig, ax = plt.subplots(1, 3) 
    ax[0].set_title("Умножение матриц") 
    ax[1].set_title("Поиск детерминанта")
    ax[2].set_title("Поворот") 

    #сравнение произведения матриц
    functions = [[square_matrix_2, [], "simple"],
                [square_matrix, [], "shtrassen"],
                [np.dot, [], "numpy"]]

    compare(ax[0], (1, 410, 200), functions)
    print(" - multication completed\n")

    #сравнение поисков детерминанта
    functions = [[determinant, [], "simple"],
                [np.linalg.det , [], "numpy"]]

    compare(ax[1], (1, 10, 1), functions, 1)
    print(" - determinant completed\n")

    #сравнение поворота
    functions = [[rotate, [], "simple"],
                [np.rot90 , [], "numpy"]]

    compare(ax[2], (1, 100, 1), functions, 1)
    print(" - determinant completed\n")

    print("COMPLETED!!!!!!!!!\n")
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
    plt.show()

#сравнение одного свойства
def compare(ax, interval, functions, arg = 2):
    start, finish, step = interval
    finish_load = random.randint(30, 80)
    size = [i for i in range(start, finish, step)]
    loading(0, finish_load)
    timer(functions, finish, step, arg)
    for func in functions: ax.plot(size, func[1], label = func[2]) 
    loading(finish_load, 101)

#cчетчик времени для функций
def timer(functions, finish, step, arg = 2):
    for i in matrix_generator(finish, step):
      for func in functions:
          start_time = time.time()
          if arg == 2: func[0](i, i)
          else: func[0](i)
          func[1].append(time.time() - start_time)

#загрузка
def loading(start, finish):
    s = '█'
    for line in range(start, finish):
        time.sleep(0.025)
        print('\r','Загрузка',(line // 3 * 2) * s,str(line),'%',end='')

develop()



