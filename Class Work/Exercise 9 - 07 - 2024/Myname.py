firstname = input(" Enter your first name: ")

lastname = input(" Enter your last name: ")

age = input(" Enter your age: ")

print(" Your Fullname is", firstname, lastname, "and your Age is ", age )

print('')
name = input(" What is your name? ")
if name:

	print("your name is ", name)
	print("Hello")
	print("Tech Blazzers")

print('')
age = int(input(" How old are you? "))

if age >= 20 and age <= 45:
	print("Hello")
	print("Tech Blazzers")
	print("your age is ", age , ", you are eligible to make your own decisions. ")
	
elif age >= 13 and age <= 19:
	print("Hello")
	print("you are a teenager")

elif age > 0 and age < 13:
	print("you are still growing up")
else:
	print("you are still a child")


