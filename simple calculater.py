#Made by somil mittal 
print("~~~~~~~TWO VALUE CALCULATER~~~~~~~")
print("Made by 'SOMIL MITTAL'")
#This are the function for all the operation.
def add(x,y):
    return num1+num2
#subtract
def sub(x,y):
    return num1-num2
#multiply
def multi(x,y):
    return num1*num2
#divide
def divi(x,y):
    return num1/num2
#mean
def mean(x,y):
    return (num1+num2)/2

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Mean")

while True:
    # take input from the user
    choice = input("enter your option from 1/2/3/4/5: ")
    # check if choice is one of the four options
    if choice in ('1','2','3','4','5'):
        try:
            num1=float(input("enter the first value: "))
            num2=float(input("enter the second value: "))
        except ValueError:
            print("invalid sentex \n enter the right value: ")
            continue
        
        if choice== '1':
            print(num1,"+",num2,"is: ",add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"is: ",sub(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"is: ",multi(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"is: ",divi(num1,num2))
        elif choice == '5':
            print("mean of num1 and num2 is: ",mean(num1,num2))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
        else:
          print("invalid input try again:")