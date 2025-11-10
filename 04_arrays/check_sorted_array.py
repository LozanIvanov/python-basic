numbers=[1,3,4,6,2]

is_sorted=True

for i in range(len(numbers)-1):
    if numbers[i]>numbers[i+1]:
        is_sorted=False
        break

if is_sorted:
    print("The array is sorted in ascending order")
else:  
     print("The array is NOT sorted in ascending order")  
