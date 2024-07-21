print("\n Application that display the smallest and the largest number with the average of both..... ")

largest_num = 0
smallest_num = 0
average = 0
product = 0

arithmetic = int(input('Enter The First number : '))
smallest = int(input('Enter The Second number : '))
largest = int(input('Enter The Third number: '))

total = arithmetic + smallest + largest
print("\n The total sum of all numbers is : ", total)

if (arithmetic > smallest) and (arithmetic > largest):
	largest_num += arithmetic
elif (smallest > arithmetic) and (smallest > largest):
	largest_num += smallest
elif (largest > arithmetic) and (largest > smallest):
	largest_num += largest
print("\n The largest of the 3 numbers is : ", largest_num)


	
if (arithmetic < smallest) and (arithmetic < largest):
	smallest_num += arithmetic

elif (smallest < arithmetic) and (smallest < largest):
	smallest_num += smallest

elif (largest < arithmetic) and (largest < smallest):
	largest_num += largest 

print("\n The smallest of the 3 numbers is : ", smallest_num)

average = (total / 3)
print("\n The avarage value of all three numbers is", average)

product = (arithmetic * smallest * largest)
print("\n The product value of all three numbers is", product)
