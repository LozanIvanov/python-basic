numbers=[3,2,5,4,6]
new_value=int(input('Въведете число, с което да се заменят четните елементи: '))

for i in range(len(numbers)):
   if numbers[i]%2==0:
      numbers[i]=new_value
print("Новият масив е:", numbers)