
'''
for i in range(1, 5):
    for j in range(1, i+1):
       print(j, end=' ')
    print()
'''
'''
for i in range(4, 0, -1):     
    for j in range(i):         
        print('*',end=' ')
    print()  
'''
'''
numbers=[2,3,4.5,6]
sum=0
for i in numbers:
    sum+=i
average = sum/len(numbers)  
print(f'{average:.2f}')
average=round(average,2) 
print(average)
'''
'''
numbers=[3,2,5,4,6]
new_value=int(input('Въведете число, с което да се заменят четните елементи: '))

for i in range(len(numbers)):
   if numbers[i]%2==0:
      numbers[i]=new_value
print("Новият масив е:", numbers)      

'''
number=[]

for i in range(5):
    num=float(input(f'Enter a number {i+1}:'))
    number.append(num)
max_number=max(number) 
if max_number.is_integer():
    print("Най-голямото число е:", int(max_number))
else:
    print(f"Най-голямото число е: {max_number}") 

                  
