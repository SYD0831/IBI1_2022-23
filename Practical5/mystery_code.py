# What does this piece of code do?
# Answer:this piece of code can randomly generate 10 numbers up to 100 and output the maximum of them

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1
#Calculate the number of random selections
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n
#use stored_random_number to store larger random numbers
print(stored_random_number)
#output the maximum
