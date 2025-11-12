def is_even(num):
    if(num%2==0):
        return True
    else:
        return False

number=int(input("Enter number bigger then 0: "))

result=is_even(number)
print(result)