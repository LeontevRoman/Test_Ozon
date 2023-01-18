test_count = int(input())

for _ in range(test_count):
    purchase_count = input()
    purchase_list = sorted(input().split())
    result = {}
    final = []
    for price in purchase_list:
        result[price] = result.get(price, 0) + 1
    for price, count in result.items():
        final.append((count - (count // 3)) * int(price))
    print(sum(final))