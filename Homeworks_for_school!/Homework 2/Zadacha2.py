stack = []

commands_ammount = int(input("Input the ammount of commands you would like to use!"))

for i in range(0,commands_ammount):
    command_input =input("Please input your command! (1,2,3,4,5)").split()
    if "1" in command_input:
        stack.append(command_input[1])
    
    elif "2" in command_input:
        if stack:
            stack.pop()
    
    #Знам че min() и max() правят stack на list, но нямам силата да правя функция която да следи кой е най големия елемнт!!!!!!!!!
    elif "3" in command_input:
        print(max(stack))
    
    else:
        print((min(stack)))

for i in stack:
    print(i,end=",")

#не е отучнено какво да се прави в случай че команда 2 е активиране, и stack е празен!
#В случай че е стека е празен и команда две се аквитира съм го направил да го просупска с проверка!!!
