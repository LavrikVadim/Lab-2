from csv import reader


def task1():
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        titles = []
        result = []
        table = reader(csvfile, delimiter=';')
        for row in table:
            titles.append(row[1])
        titles.remove('Название')
        for i in titles:
            if len(i) > 30:
                result.append(i)
        print(len(result))



def task2(): 
    author = input()
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
            books = []
            authors = []
            result = []
            table = reader(csvfile, delimiter=';')
            for row in table:
                if author == row[3]:
                    authors.append(row)
            for i in authors:
                if float(i[7]) > 200:
                    result.append(i[1])
            if len(set(result)) > 0:
                print(set(result))
            else:
                print('Таких книг не нашлось. Попробуйте указать другого автора')
       
      
       

