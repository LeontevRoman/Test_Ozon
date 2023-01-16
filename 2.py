test_count = int(input())


for _ in range(test_count):
    purchase_count = input()
    purchase_list = input().split()
    result = 0
    for price in set(purchase_list):
        count = purchase_list.count(price)
        result += (count - (count // 3)) * int(price)
    print(result)
    