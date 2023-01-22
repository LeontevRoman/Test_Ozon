import time
from _5_test_input_data import test_count, count_iterable, list_count

test_count = test_count
start = time.time()

for _ in range(test_count):
    count_iterable = count_iterable
    flag = 'YES'
    list_count = [_ for _ in list_count.split()]
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

end = time.time()
print("The time of execution of above program is :", (end-start) * 10**3, "ms")