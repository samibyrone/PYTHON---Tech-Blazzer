print(" Application that calculate your investment with interest over a period of 10years till 30years..... ")

principal_amount = int(input(f" Enter your Investment Deposit amount: "))

# principal_amount = $1000

annual_rate = 7/100

amount_at_the_end_of_the_years = 0

years = 0


amount_at_the_end_of_the_years == (principal_amount * (1 + annual_rate) ** years)

for num in range(1, 30):	
	print(f' Total amount for years', years , 'is', amount_at_the_end_of_the_years)