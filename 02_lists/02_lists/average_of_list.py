numbers=[2,3,4.5,6]
sum=0
for i in numbers:
    sum+=i
average = sum/len(numbers)  
print(f'{average:.2f}')
average=round(average,2) 
print(average)