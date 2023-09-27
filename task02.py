# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой
# длины: имена str, ставка int, премия str с указанием процентов вида "10.25%".
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def my_generator(names, rates, percents):  # Генератор, в соответствии с заданием
    if (len(names) == len(rates)) and (len(names) == len(percents)):
        return dict(
            zip(
                names, list(
                    map(lambda r, p:
                        r * (1 + float(p.replace('%', '').replace(',', '.')) / 100),
                        rates, percents
                        )
                )
            )
        )
    else:
        raise IndexError("Length of names, rates or percents is do not match")


if __name__ == '__main__':
    list1 = ['Петя',
             'Вася',
             'Коля',
             'Маша',
             ]
    list2 = [10,
             20,
             30,
             40,
             ]
    list3 = ['10.25%',
             '40%',
             '5,45',
             '16',
             ]

    try:
        for i in range(len(list1)):
            print(f'{list1[i]}\t{list2[i]}\t{list3[i]}')
        print('=================')
        print(my_generator(list1, list2, list3))
    except IndexError:
        print('Не совпадают размеры списков!')


# Результат работы:
# C:\Work\python\dz4\Py4HW05\venv\Scripts\python.exe C:/Work/python/dz4/Py4HW05/task02.py
# Петя	10	10.25%
# Вася	20	40%
# Коля	30	5,45
# Маша	40	16
# =================
# {'Петя': 11.025, 'Вася': 28.0, 'Коля': 31.634999999999998, 'Маша': 46.4}
#
# Process finished with exit code 0
