import time
from _2_test_input_data import count_iterable, count_purchase, list_purchase

test_count = int(count_iterable)

'''start = time.time()
for _ in range(test_count):
    purchase_count = count_purchase
    purchase_list = list_purchase.split()
    result = []
    print(purchase_list)
    for price in set(purchase_list):
        count = purchase_list.count(price)
        result.append(count)
    print(result)
end = time.time()
print("The time of execution of above program is :", (end-start) * 10**3, "ms")
print()'''

start = time.time()
for _ in range(test_count):
    purchase_count = count_purchase
    purchase_list = sorted(list_purchase.split())
    result = {}
    final = []
    for price in purchase_list:
        result[price] = result.get(price, 0) + 1
    for price, count in result.items():
        final.append((count - (count // 3)) * int(price))
print(sum(final))

end = time.time()
print("The time of execution of above program is :", (end-start) * 10**3, "ms")