#def consonant_and_vowel(name):


name = input("\n Enter any name of your choice to determine the number of vowels and consonants counts: ")

vowel = "" 
consonant = ""

for character in name:
	if character.lower() in ['a', 'e', 'i', 'o', 'u']:
		vowel += character

	else :
		consonant += character

print(f" There are {len(set(vowel))} vowels and {len(set(consonant))} consonant ")

#print(consonant_and_vowel(abimbola))
#print(consonant_and_vowel(olarewaju))
