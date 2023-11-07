food= int(input("Input how much food you have!"))
# Правим си input за да въведем цялата храна.
orders = list(map(int, input("Input your orders!").split()))
#Тука list превърща map обекта в лист; map прави всички елементи в inputa да са  int; .split() разделя stringa.
served = 0
remaining_orders = []
# Дефинираме празен лист

# Правим цикъл.
for i in orders: 
    # Проверяваме дали food е по-голямо и или равно на i (i може да си го представите като една невидима точка която минава през всеки елемнт на листа започаваща от първият.)
    if food>= i:
        # Ако минем през проверката стават следните неща: От food се маха i;  Добавяаме 1 към served
        food -= i
        served += 1
    else:
        #Ако не мине през проверката ще мине през тази, и ще  се спре цикълът чрез break(утре ще ви обясня как бачка orders[served:])

        remaining_orders = orders[served:]
        break

print(max(orders))
#Принтираме най-голямто число в orders

if served == len(orders):
    #Ако стойноста на served (число) е равна на броя елемнти в листът orders, тогава се минава проверката.
    print("Orders complete") 
else:
    #Ако не мине през първата проверка, ще мине през тази и ще се принитра това долу.
    print("Remaining orders:", ", ".join(map(str, remaining_orders)))
    # "," служи за да разделия елементие; map служи да направи всички елемнти от листът на  strings