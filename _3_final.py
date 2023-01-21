
for _ in range(int(input())):
    count_developers = int(input())
    list_developers_status = [int(_) for _ in input().split()]
    developers_list = [_ for _ in range(count_developers)]
    while developers_list:
        first = list_developers_status[developers_list[0]]
        min_status = 100
        delete_number = 0
        count = 1
        for i in developers_list[1:]:
            second = list_developers_status[i]
            if first == second:
                delete_number = count
                break
            else:
                if abs(second - first) < min_status:
                    min_status = abs(second - first)
                    delete_number = count
            count += 1
        print(developers_list[0] + 1, developers_list[delete_number] + 1)
        developers_list.pop(delete_number)
        developers_list.pop(0)
    print()
