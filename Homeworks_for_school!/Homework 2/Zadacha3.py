
food= int(input())
orders = list(map(int, input().split()))

served = 0
remaining_orders = []

for order in orders:
    if food>= order:
        food -= order
        served += 1
    else:
        remaining_orders = orders[served:]
        break

print(max(orders))

if served == len(orders):
    print("Orders complete")
else:
    print("Remaining orders:", ", ".join(map(str, remaining_orders)))