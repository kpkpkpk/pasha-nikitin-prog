import random
import math

#рандомное заполнение
def rand(length):
    result = []

    for i in range(length):
        result.append([])
        for j in range(length):
            a = random.randint(1, 30)
            result[-1].append(a)
    return result

#мат ожидание
def math_waiting(array):
   for i in array:
       math = 0
       row = i.copy()
       row.sort()
       index = 0
       while index < len(row):
           count = 0
           while index < len(row) - 1 and row[index] == row[index + 1]:
               count += 1
               index += 1
           math += row[index - count] * (count + 1) / len(row)
           index += 1
       print("Math_waiting: " + str(math))
   print("\n")

#дисперсия
def disperssion(array):
   for row in array:
       average = sum(row) / len(array)
       result = 0
       for j in row: result += math.sqrt(pow(j - average, 2))
       print("Disperssion: " + str(result))
   print("\n")

#красивый вывод
def Print(data):
    print("YOUR MATRIX: ")
    col_width = max(word for row in data for word in row)
    for row in data:
       print(" ".join(str(word).ljust(len(str(col_width))) for word in row))
    print("\n")

print("Enter a size: ")
size = int(input())
array = rand(size)
Print(array)
disperssion(array)
math_waiting(array)