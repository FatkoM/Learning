stack = []

while True:
    un_pade = input("Input the customers! ")

    if un_pade == "PAID":
        for i in range(len(stack)):
            stack.pop()

    elif un_pade == "END":
        for i in stack:
            print(i)
        
        print(f"{len(stack)} people remaining! ")
        exit()

    else:
        stack.append(un_pade)