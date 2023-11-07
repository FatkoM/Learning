stack = []

biggest_num = 0
smallest_num = 0
commands_ammount = int(input("Input the ammount of commands you would like to use!"))

def max_and_min_calc():
    global biggest_num
    global smallest_num
    for i in stack:
                if i > biggest_num:
                    biggest_num = i
                
                elif i < smallest_num:
                    smallest_num = i

for i in range(0,commands_ammount):
    command_input =input("Please input your command! (1,2,3,4,5)").split()
    if "1" in command_input:
        if not stack:
            biggest_num = int(command_input[1])
            smallest_num = int(command_input[1])
        
        else:
            max_and_min_calc()

        stack.append(int(command_input[1]))
    
    elif "2" in command_input:
        if stack:
            if int(command_input[0]) == biggest_num or smallest_num:
                stack.pop()
                max_and_min_calc()

    elif "3" in command_input:
        print(biggest_num)
    
    elif "4" in command_input:
        print(smallest_num)
    
    else:
        print(len(stack))

for i in stack:
    print(i,end=",")

#не е отучнено какво да се прави в случай че команда 2 е активиране, и stack е празен!
#В случай че е стека е празен и команда две се аквитира съм го направил да го просупска с проверка!!!
