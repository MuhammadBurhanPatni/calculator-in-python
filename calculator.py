def calculator() :
    a :int = int(input("Enter the First Number :"))
    b :int = int(input("Enter the Second Number :"))
    operations= ["Addition","Subtraction","Multiplication","Division"]
    for i,operation in enumerate(operations) :
        print(f"{i+1}.{operation}")

    choice:int = input("Enter The Number Between(1-4) To Select The Operation :")

    if choice == "1" :
        result :int = a + b
        print(f"{a} + {b} = {result}") 

    elif choice == "2" :
        result :int = a - b
        print(f"{a} - {b} = {result}") 

    elif choice == "3" :
        result :int = a*b
        print(f"{a} * {b} = {result}")

    elif choice == "4" :
        result :int = a / b
        print(f"{a} / {b} = {result}")
    else :
        print("Enter a valid Number")
calculator()      