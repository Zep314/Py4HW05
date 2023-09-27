# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os


def get_file_components(path):
    """
    Функция возвращает кортеж, содержащий путь, имя и расширение файла
    :param path:  Полный пусть к файлу + имя с расширением
    :return: (<путь к файлу>, <имя файла>, <расширение файла>)
    """
    return (
        '' if path.rfind(os.sep) == -1 else path[:path.rfind(os.sep)],  # Путь к файлу
        path.split(os.sep)[-1].split('.')[0],                           # Имя файла
        '' if path.find('.') == -1 else path.split('.')[-1]             # Расширение файла
    )


if __name__ == '__main__':  # Сама программа

    path_to_file = 'C:\\Windows\\System32\\drivers\\etc\\lmhosts.sam'
    print('=================')
    print(f'path_to_file: {path_to_file}')
    print(f'Path components: {get_file_components(path_to_file)}')

    path_to_file = 'lmhosts.sam'
    print('=================')
    print(f'path_to_file: {path_to_file}')
    print(f'Path components: {get_file_components(path_to_file)}')

    path_to_file = 'C:\\Windows\\System32\\drivers\\etc\\lmhosts'
    print('=================')
    print(f'path_to_file: {path_to_file}')
    print(f'Path components: {get_file_components(path_to_file)}')

# Результат работы:
# C:\Work\python\dz4\Py4HW05\venv\Scripts\python.exe C:/Work/python/dz4/Py4HW05/task01.py
# =================
# path_to_file: C:\Windows\System32\drivers\etc\lmhosts.sam
# Path components: ('C:\\Windows\\System32\\drivers\\etc', 'lmhosts', 'sam')
# =================
# path_to_file: lmhosts.sam
# Path components: ('', 'lmhosts', 'sam')
# =================
# path_to_file: C:\Windows\System32\drivers\etc\lmhosts
# Path components: ('C:\\Windows\\System32\\drivers\\etc', 'lmhosts', '')
#
# Process finished with exit code 0
