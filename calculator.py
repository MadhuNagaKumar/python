i=1
while i==1:
    try:
        a=float(input("Enter the first value: "))
        i=i+1
    except:
        print('Oops!')
        print('Run again')
i=1
while i==1:
    try:
        b=float(input("Enter the second value: "))
        i=i+1
    except:
        print('Oops!')
        print('Run again')
i=1
while i==1:
    print("1.Addition\n2.Subraction\n3.Multiplication\n4.Division\n5.Power")
    choi=float(input("Enter your choice: "))
    choi=round(choi)
    if choi==1:
        print("The added value is:",a+b)
        i=i+1
    elif choi==2:
        print("The subracted value is :",a-b)
        i=i+1
    elif choi==3:
        print("The Multiplicated value is:",a*b)
        i=i+1
    elif choi==4:
        if b==0:
            print("infinite")
        else:
            print("The dived value is:",a/b)
        i=i+1
    elif choi==5:
        print("The a power b is:",a**b)
        i=i+1
    else:
        print("Invalid option\nchoose corectly")
