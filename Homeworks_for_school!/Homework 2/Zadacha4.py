#clothes_in_order e функция която изъврша този блок код. Pile и Capacity  са променливии (аргументи) които са деклалирани по долу!
def clothes_in_order(pile, capacity):#
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

clothes_pile = list(map(int, input("Input the clothe_piles!").split())) #Тука list превърща map обекта в лист; map прави всички елементи вinputa да са  int; .split() разделя stringa"*
shelf_capacity = int(input("Input the capacity!"))


print(clothes_in_order(clothes_pile, shelf_capacity)) #викаме функцията