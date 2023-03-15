#Question:	How	long	until	I	run	out?
#Function: breed 100
number_rabbit = 2
generation = 1
#	Repeat:
while number_rabbit <= 100:
#	Check if there are enough rabbits
#	if no: keep breeding
#	calculate the number of newborn rabbits
	number_new = number_rabbit
#	calculate the total number of rabbits
	number_rabbit = number_rabbit + number_new
#	Calculate the number of generations
	generation += 1
#If yes: output result
generation_out = str(generation)
print("the",generation_out,"st genoration has more than 100 rabbits") 

#the result of these codes :the 7 st genoration has more than 100 rabbits

