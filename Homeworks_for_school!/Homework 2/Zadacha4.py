def clothes_in_order(pile, capacity):
    shelves = 0
    current_shelf_capacity = capacity

    for clothes in pile:
        if clothes > current_shelf_capacity:
            shelves += 1
            current_shelf_capacity = capacity - clothes
        else:
            current_shelf_capacity -= clothes

    if current_shelf_capacity < capacity:
        shelves += 1
    
    return shelves

clothes_pile = list(map(int, input("Input the clothe_piles!").split()))
shelf_capacity = int(input("Input the capacity!"))


print(clothes_in_order(clothes_pile, shelf_capacity))