food= int(input("Input how much food you have!"))
orders = list(map(int, input("Input your orders!").split()))
#Тука list превърща map обекта в лист; map прави всички елементи в inputa да са  int; .split() разделя stringa.
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
    # "," служи за да разделия елементие; map служи да направи всички елемнти от листът на  strings