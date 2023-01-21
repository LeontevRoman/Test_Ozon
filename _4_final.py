
count_test = int(input())

for _ in range(count_test):
    input()
    i , j = input().split() #считываем размер
    table_tuples = ([[int(_) for _ in input().split()] for _ in range(int(i))]) #заполняем матрицу

    count_click = int(input())
    for list_click in input().split():
        table_tuples.sort(key=lambda table: table[int(list_click)-1]) #сортируем по введенному столбцу

    for k in range(int(i)):
        print(*table_tuples[k])
    print()