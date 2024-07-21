heart_rate = input("Kindly Enter Age Range: ")

maximum_heart_rate = 220
health_check = 85 / 100
health_check2 = 50 / 100

heart_rate -= maximum_heart_rate
rate = float(heart_rate)

if rate >= health_check2 and rate <= health_check:
	print("\n Congratulations! Your heart rate is in good condition. ")

elif rate >= health_check:
	print("\n Your Heart Rate Is Too High Kindly Visit Your Doctor For a Check-up Soon! ")

elif rate <= health_check2:
	print("\n Your Health Is At Risk, Pay More Attention To It And Do The Needful Sooner1 ")

else:
	print(' Error!!! Wrong input, Please try better next time... ')
