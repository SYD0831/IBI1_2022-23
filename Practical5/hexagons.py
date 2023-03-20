#Function: hexagons
#Use the for loop to output the values we need in turn.
#Use the range function to determine our output range
#use the the formula for the nth hexagonal number
#Output sequence


h = 1
for n in range(1,6):
 h = 2*n*(2*n-1)*0.5
 print("The",n,"st hexagon number is",h)









#Another method:
#    Every number of the sequence of hexagons can be viewed as the sum of several elements.
#    Number of elements
#n = 1
#for n in range(1,6):
#     number_elements = n	#    Numerical serial number
#     differ_elements = 4	#    The difference between elements
#     value_elements = 1
#     value_tria = 1
#     The value of each element
#     while  number_elements != 1:
#         value_elements = value_elements + differ_elements
#         number_elements = number_elements-1
#         value_tria = value_tria + value_elements	#    the values of the triangle sequence
#     print("The",n,"st hexagon number is",value_tria)




#the output of the py.file
#The 1 st hexagon number is 1
#The 2 st hexagon number is 6
#The 3 st hexagon number is 15
#The 4 st hexagon number is 28
#The 5 st hexagon number is 45
#we can change the rang(1,a+1) to print out a value

