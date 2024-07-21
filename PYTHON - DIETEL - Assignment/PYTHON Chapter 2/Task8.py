print("\n Application That Display The Smallest, Largest Number With The Average And The Product..... ")

largest_num = 0
smallest_num = 0
average = 0
product = 0

arithmetic = int(input('Enter The First number : '))
smallest = int(input('Enter The Second number : '))
largest = int(input('Enter The Third number: '))
extra = int(input('Enter the fourth numbr: '))

total = arithmetic + smallest + largest + extra
print("\n The Total Sum Of All Numbers is : ", total)

if (arithmetic > extra) and (arithmetic > largest) and (arithmetic > smallest):
	largest_num += arithmetic

elif (smallest > arithmetic) and (smallest > largest) and (smallest > extra):
	largest_num += smallest

elif (largest > arithmetic) and (largest > smallest) and (largest > extra):
	largest_num += largest

elif (extra > arithmetic) and (extra > smallest) and (extra > largest):
	largest_num += extra

print("\n The largest Of The 3 Numbers is : ", largest_num)


	
if (arithmetic < smallest) and (arithmetic < largest) and (arithmetic < extra):
	smallest_num += arithmetic

elif (smallest < arithmetic) and (smallest < largest) and (smallest < extra):
	smallest_num += smallest

elif (largest < arithmetic) and (largest < smallest) and (largest < extra):
	largest_num += largest 

elif (extra < arithmetic) and (extra < largest) and (extra < smallest):
	largest_num += extra 

print("\n The Smallest Of The 4 Numbers is : ", smallest_num)

average = (total / 4)
print("\n The Avarage Value Of All Four Numbers is", average)

product = (arithmetic * smallest * largest * extra)
print("\n The Product Value Of All Four Numbers is", product)
