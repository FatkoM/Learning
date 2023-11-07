#clothes_in_order e функция която изъврша този блок код. Pile и Capacity  са променливии (аргументи) които са деклалирани по долу!
piles = list(map(int, input("Input the clothes piles (separated by spaces): ").split()))
capacity = int(input("Input the shelf capacity:"))

shelves = 0
current_shelf = capacity

for clothes in piles:
    if clothes > current_shelf:
        shelves += 1
        #STIGA SI PREPISVAL SASHEEEEEEE
        current_shelf = capacity - clothes
    else:
        current_shelf -= clothes

if current_shelf < capacity:
    shelves += 1

print(f"Number of shelves required: {shelves}")