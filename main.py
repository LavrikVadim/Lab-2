from csv import reader


# flag = 0
# output = open('result.txt', 'w')
# search = input('Search for: ')
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
       
task2()       
       
       
        #      books.append(row)
        # books.remove(books[0])
        # for i in books:
        #     
             
        
#         lower_case = row[2].lower()
#         index = lower_case.find(search.lower())
#         if index != -1:
#             print(row[2])
#             flag = 1
#             output.write(f'{row[0]}. {row[2]}. Цена {row[8]} рублей.\n')

#     if flag == 0:
#         print('Nothing found.')

# output.close()

# with open('books.csv') as f:
#     table = reader(f, delimiter=';')
#     for row in table:
#         print(row)