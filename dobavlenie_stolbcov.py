import pandas


def vivesti_stolbec_faila(path, extension, stolbec):
    """Функция для вывода одного или нескольких столбцов из файла Excel в "path" нужно прописать путь до файла без
    расширения. Пример - ('C:/Users/USER/Desktop/1') в "extension" нужно прописать расширение файла. Пример - ('.xls)
    в "stolbec" нужно прописать необходимые столбцы. Пример "A, C, E:J" либо можно написать наименования столбцов (
    "company", "rank", "revenues") """
    file = path + extension
    data = pandas.read_excel(file, usecols=stolbec)
    return data

help(vivesti_stolbec_faila)

df = vivesti_stolbec_faila(r'C:/Users/USER/Desktop/1', '.xls', 'A, D')

print("\n--- список всех столбцов в вытащеном файле ---\n", df.columns.tolist())

