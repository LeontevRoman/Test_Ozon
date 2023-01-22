test_count = int(input())

for _ in range(test_count):
    count_iterable = input()
    flag = 'YES'
    list_count = [_ for _ in input().split()]
    final = {list_count[0]:1}
    for i in range(1, int(len(list_count))):
        if list_count[i] == list_count[i-1]:
            continue
        else:
            final[list_count[i]] = final.get(list_count[i], 0) + 1
            if final[list_count[i]] > 1:
                flag = 'NO'
                break
    print(flag)
