
import glob
import os


def dir_find(path, extension):

    if not os.path.exists(path):
        return print('Каталог не найден')

    files = glob.glob(path + '**/*.' + extension, recursive=True)
    return print(files)


path1 = input('Введите путь до каталога (например C:/../): ')
extension1 = input('Введите расширение файла (например txt): ')
dir_find(path1, extension1)