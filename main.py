import random
from pprint import pprint
import sys
x = 'X'
o = 'O'
len_x = []
element = range(1, 101)
filed = []
closed_filed = []


def field_game():
    for i in range(10):
        c = [element[0+ i*10], element[1+ i*10], element[2+ i*10], element[3+ i*10], element[4+ i*10], element[5+ i*10],
               element[6+ i*10], element[7+ i*10],  element[8+ i*10], element[9+ i*10]]
        filed.append(c)

def player_move():
    try:
        question = int(input('Выбери поле от 1 до 100:'))
        if question not in closed_filed:
            for key, element in enumerate(filed):
                for n, el in enumerate(element):
                    if el == question:
                        closed_filed.append(element[n])
                        element[n] = x
        elif question in closed_filed:
            print('занято, попробуй другую клетку')
            player_move()
    except ValueError:
        print('Некорректный ввод. Введите число от 1 до 100')
        player_move()


def first():
    filed_comp = range(1, 101)
    num_to_select = 1
    list_of_random_items = random.sample(filed_comp, num_to_select)
    first_random_item = list_of_random_items[0]
    if first_random_item not in closed_filed:
        for key, element in enumerate(filed):
            for n, i in enumerate(element):
                if i == first_random_item:
                    closed_filed.append(element[n])
                    element[n] = o
                    break

def check_or_lose():
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                if 0 <= i+4 < 10 and filed[n][i] == x and filed[n][i + 1] == x and filed[n][i + 2] == x and filed[n][i + 3] == x and filed[n][i + 4] != o and filed[n][i + 4] != x:
                    closed_filed.append(filed[n][i + 4])
                    filed[n][i + 4] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                if 0 <= i-1 < 10 and 0 <= i+4 < 10 and filed[n][i] == x and filed[n][i + 1] == x and filed[n][i + 2] == x and filed[n][i + 3] == x and filed[n][i + 4] == o and filed[n][i - 1] != x:
                    closed_filed.append(filed[n][i - 1])
                    filed[n][i - 1] = o
                    return True
                elif 0<= n <10 and 0 <= i+3 < 10 and filed[n][i] == 'X' and filed[n][i + 1] == 'X' and filed[n][i + 2] == 'X' and filed[n][i + 3] == 'X' and filed[n][i -1] != o and filed[n][i -1] != x:
                    closed_filed.append(filed[n][i - 1])
                    filed[n][i - 1] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                k = n + 4
                if 0 <= k < 10 and 0 <= k - 3 < 10 and 0 <= n - 1 < 10 and filed[n][i] == x and filed[k - 3][
                    i] == x and filed[k - 2][i] == x and filed[k - 1][i] == x and filed[k][i] == o and filed[n - 1][
                    i] != x:
                    closed_filed.append(filed[n - 1][i])
                    filed[n - 1][i] = o
                    return True
                elif 0 <= k - 1 < 10 and 0 <= n - 1 < 10 and filed[n][i] == x and filed[k - 3][i] == x and filed[k - 2][i] == x and filed[k - 1][i] == x and filed[n - 1][i]!=o and filed[n - 1][i] != x:
                    closed_filed.append(filed[n - 1][i])
                    filed[n - 1][i] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                k = n + 4
                if 0 <= k < 10 and 0 <= k - 3 < 10 and filed[n][i] == x and filed[k - 3][i] == x and filed[k - 2][
                    i] == x and filed[k - 1][i] == x and filed[k][i] != o and filed[k][i] != x:
                    closed_filed.append(filed[k][i])
                    filed[k][i] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                k = n + 4
                l = i - 4
                if 0 <= k < 10 and 0 <= l < 10 and filed[n][i] == x and filed[n + 2][i - 2] == x and filed[n + 1][
                    i - 1] == filed[k - 1][i - 3] == x and filed[k][i - 4] != o and filed[k][i - 4] != x:
                    closed_filed.append(filed[k][i - 4])
                    filed[k][i - 4] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                k = n + 4
                l = i - 4
                if 0 <= k < 10 and 0 <= l < 10 and filed[n][i] == x and filed[n + 2][i - 2] == x and filed[n + 1][
                    i - 1] == filed[k - 1][i - 3] == x and filed[k][i - 4] == o and filed[n - 1][i + 1] != x:
                    closed_filed.append(filed[n - 1][i + 1])
                    filed[n - 1][i + 1] = o
                    return True
                elif 0 <= k-1 < 10 and 0 <= i-3 < 10 and filed[n][i] == x and filed[n + 2][i - 2] == x and filed[n + 1][
                    i - 1] == filed[k - 1][i - 3] == x and filed[n - 1][i + 1] != x:
                    closed_filed.append(filed[n - 1][i + 1])
                    filed[n - 1][i + 1] = o
                    return True

    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                k = n - 4
                l = i - 4
                if 0 <= k < 10 and 0 <= l < 10 and filed[n][i] == x and filed[n - 1][i - 1] == filed[(n - 4) + 1][
                    (i - 4) + 1] == x and filed[n - 2][i - 2] == x and filed[n - 4][i - 4] != o and filed[n - 4][
                    i - 4] != x:
                    closed_filed.append(filed[n - 4][i - 4])
                    filed[n - 4][i - 4] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                k = n - 4
                if 0 <= k < 10 and 0 <= i + 1 < 10 and 0 <= i - 4 < 10 and 0 <= n + 1 < 10 and filed[n][i] == x and \
                        filed[n - 1][i - 1] == filed[k + 1][(i - 4) + 1] == x and filed[n - 2][i - 2] == x and \
                        filed[k][i - 4] == o and filed[n + 1][i + 1] != x:
                    closed_filed.append(filed[n + 1][i + 1])
                    filed[n + 1][i + 1] = o
                    return True
                elif 0 <= n+4 < 10 and 0 <= i + 4 < 10 and filed[n][i] == filed[n + 1][i + 1] == filed[n+2][i +2] == filed[n + 3][i +3] == x and filed[n+4][i + 4] != x and filed[n+4][i + 4] != o:
                    closed_filed.append(filed[n+4][i + 4])
                    filed[n+4][i + 4] = o
                    return True
        return False

def II_move():
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                if 0 <= i - 1 < 10 and 0 <= i < 10 and 0 <= i + 1 < 10 and filed[n][i] == o and filed[n][i - 1] != x and \
                        filed[n][i - 1] != o and filed[n][i + 1] == x:
                    closed_filed.append(filed[n][i - 1])
                    filed[n][i - 1] = o
                    return True
                elif 0 <= i - 1 < 10 and 0 <= i < 10 and filed[n][i] == o and filed[n][i - 1] != x and filed[n][
                    i - 1] != o:
                    closed_filed.append(filed[n][i - 1])
                    filed[n][i - 1] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                if 0 <= i + 1 < 10 and 0 <= i < 10 and 0 <= i - 1 < 10 and filed[n][i] == o and filed[n][i + 1] != o and \
                        filed[n][i + 1] != x and filed[n][i - 1] == x:
                    closed_filed.append(filed[n][i + 1])
                    filed[n][i + 1] = o
                    return True
                elif 0 <= i + 1 < 10 and 0 <= i < 10 and filed[n][i] == o and filed[n][i + 1] != o and filed[n][
                    i + 1] != x:
                    closed_filed.append(filed[n][i + 1])
                    filed[n][i + 1] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                if 0 <= i < 10 and 0 <= n - 1 < 10 and 0 <= n + 1 < 10 and filed[n][i] == o and filed[n - 1][i] != o and \
                        filed[n - 1][i] != x and filed[n + 1][i] == x:
                    closed_filed.append(filed[n - 1][i])
                    filed[n - 1][i] = o
                    return True
                elif 0 <= i < 10 and 0 <= n - 1 < 10 and filed[n][i] == o and filed[n - 1][i] != o and filed[n - 1][
                    i] != x:
                    closed_filed.append(filed[n - 1][i])
                    filed[n - 1][i] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                if 0 <= i < 10 and 0 <= n + 1 < 10 and 0 <= n - 1 < 10 and filed[n][i] == o and filed[n + 1][i] != o and \
                        filed[n + 1][i] != x and filed[n - 1][i] == x:
                    closed_filed.append(filed[n + 1][i])
                    filed[n + 1][i] = o
                    return True
                elif 0 <= i < 10 and 0 <= n + 1 < 10 and filed[n][i] == o and filed[n + 1][i] != o and filed[n + 1][
                    i] != x:
                    closed_filed.append(filed[n + 1][i])
                    filed[n + 1][i] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                if 0 <= i - 1 < 10 and 0 <= n + 1 < 10 and 0 <= n - 1 < 10 and 0 <= i + 1 < 10 and filed[n][i] == o and \
                        filed[n + 1][i - 1] != o and filed[n + 1][i - 1] != x and filed[n - 1][i + 1] == x:
                    closed_filed.append(filed[n + 1][i - 1])
                    filed[n + 1][i - 1] = o
                    return True
                elif 0 <= i - 1 < 10 and 0 <= n + 1 < 10 and filed[n][i] == o and filed[n + 1][i - 1] != o and \
                        filed[n + 1][i - 1] != x:
                    closed_filed.append(filed[n + 1][i - 1])
                    filed[n + 1][i - 1] = o
                    return True
    for key, element in enumerate(filed):
        for n, el in enumerate(element):
            for i in range(10):
                if 0 <= i - 1 < 10 and 0 <= n + 1 < 10 and 0 <= n - 1 < 10 and 0 <= i + 1 < 10 and filed[n][i] == o and \
                        filed[n - 1][i + 1] != o and filed[n - 1][i + 1] != x and filed[n + 1][i - 1] == x:
                    closed_filed.append(filed[n - 1][i + 1])
                    filed[n - 1][i + 1] = o
                    return True
                elif 0 <= n - 1 < 10 and 0 <= i + 1 < 10 and filed[n][i] == o and filed[n - 1][i + 1] != o and \
                        filed[n - 1][i + 1] != x:
                    closed_filed.append(filed[n - 1][i + 1])
                    filed[n - 1][i + 1] = o
                    return True
        return False

def II():
    len_x = []
    for element in filed:
        for el in element:
            if el == x:
                len_x.append(el)
    number_x = len(len_x)
    if number_x == 1:
        first()
    if 2 <= number_x < 50:
        II_move()
    if number_x > 3:
        check_or_lose()

def WIN():
    for n, element in enumerate(filed):
        for i in range(10):
            if 0 <= i+4 < 10 and filed[n][i] == x and filed[n][i + 1] == x and filed[n][i + 2] == x and filed[n][i + 3] == x and filed[n][i + 4] == x:
                sys.exit('Ты победил!!!')
    for n, element in enumerate(filed):
        for i in range(10):
            k = n + 4
            if 0 <= k < 10 and filed[n][i] == x and filed[k - 3][i] == x and filed[k - 2][i] == x and filed[k - 1][i] == x and filed[k][i] == x:
                sys.exit('Ты победил!!!')
    for n, element in enumerate(filed):
        for i in range(10):
            k = n + 4
            l = i - 4
            if 0 <= k < 10 and 0 <= l < 10 and filed[n][i] == filed[k][l] == x and filed[n + 2][i - 2] == x and filed[n + 1][i - 1] == filed[k - 1][i - 3] == x:
                sys.exit('Ты победил!!!')
    for n, element in enumerate(filed):
        for i in range(10):
            k = n - 4
            l = i - 4
            if 0 <= k < 10 and 0 <= l < 10 and filed[n][i] == filed[k][l] == x and filed[n - 1][i - 1] == filed[k + 1][(i - 4) + 1] == x and filed[n - 2][i - 2] == x:
                sys.exit('Ты победил!!!')
    for n, element in enumerate(filed):
        for i in range(10):
            if 0 <= i+4 < 10 and filed[n][i] == o and filed[n][i + 1] == o and filed[n][i + 2] == o and filed[n][i + 3] == o and filed[n][i + 4] == o:
                sys.exit('Победа за искусственным интеллектом')
    for n, element in enumerate(filed):
        for i in range(10):
            k = n + 4
            if 0 <= k < 10 and filed[n][i] == o and filed[k - 3][i] == o and filed[k - 2][i] == o and filed[k - 1][i] == o and filed[k][i] == o:
                sys.exit('Победа за искусственным интеллектом')
    for n, element in enumerate(filed):
        for i in range(10):
            k = n + 4
            if 0 <= k < 10 and 0 <= i-4 < 10 and filed[n][i] == filed[k][i - 4] == o and filed[n + 2][i - 2] == o and filed[n + 1][i - 1] == filed[k - 1][i - 3] == o:
                sys.exit('Победа за искусственным интеллектом')
    for n, element in enumerate(filed):
        for i in range(10):
            k = n - 4
            l = i - 4
            if 0 <= k < 10 and 0 <= l < 10 and filed[n][i] == filed[k][l] == o and filed[n - 1][i - 1] == filed[k + 1][l + 1] == o and filed[n - 2][i - 2] == o:
                sys.exit('Победа за искусственным интеллектом')
    return False



def main():
    count=0
    field_game()
    pprint(filed)
    for element in range(50):
        if count % 2 == 0:
            player_move()
            count+=1
        if count % 2 != 0:
            II()
            count += 1
        if count > 8:
            WIN()
        pprint(filed)
    else:
        print('Ничья')



main()








