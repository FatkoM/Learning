piles = list(map(int, input("Input the i piles (separated by spaces): ").split()))
#Правим input за да искаме за всички купчини с дрехи; map служи да направи всички елемнти от листът на  int
capacity= int(input("Input the shelf current_capacity:"))

current_capacity = capacity
shelves = 0

#Почваме цикъл 
for i in piles:
    if i > current_capacity:
        # Ако i е по-голямо от current_capacity, тогава се минава през проверката; След това към shelves се прибавя 1 и от current_capacity се маха i
        shelves += 1
        #STIGA SI PREPISVAL SASHEEEEEEE
        current_capacity = capacity - i
    else:
        # Ако не мине през проверката, ше дойде тук, където от current_capacity ще сме махне i.
        current_capacity -= i


# Проверяваме дали current_Capacity < capacity.
if current_capacity < capacity:
    shelves += 1

print(f"Number of shelves required: {shelves}")