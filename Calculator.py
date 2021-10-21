num1=float(input("enter first number :"))
num2=float(input("enter second number :"))
str=('''choose:
1.Addition
2."Subtraction
3."Multiplication
4".Divide''')
print(str)      
choose=int(input('enter chose 1/2/3/4:')) 
print("your choose")
if choose==1:
    print("1.addiction")
elif choose==2:
    print("2.subtraction")
elif choose==3:
    print("multiplication")
elif choose==4:
    print("divide")
else:
    print("you do not select anythinng")                    
print(num1)
print(num2)
if choose==1:
    add=num1+num2
    print(add)
elif choose==2:
    subtract=num1-num2
    print(subtract)
elif choose==3:
    multiply=num1*num2
    print(multiply) 
elif choose==4:
    divide=num1/num2
    print(divide)
else:
    print("syntax error")    