#You need to enter your cost here
#you can change the variable number_list
cost = [1,8,15,7,5,14,43,40]
number_list = cost

#You need to enter your place and year here
#you can change the variable place
place = ['Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012']


#creat a dictionary to ralated the cost and place
#Give variable lable correct value
#Sort the numbers in the list
#correct the place in correct turn
#print the sorted list 

#draw the figure
# Set the custom colors and labels
# Create the bar plot
# Add color to bar
# Add the labels to the y-axis
# Add a title and labels to the x and y axes
# Add the x, y axin lables 
# Display the plot

my_dict = dict(zip(number_list, place))
labels = []
number_list.sort()
for i in number_list:
    labels.append(my_dict[i])

print("Sorted list: ", number_list)


import matplotlib.pyplot as plt         
colors = ['violet', 'indigo', 'blue', 'lime', 'green', 'yellow', 'orange', 'red']
plt.barh(range(len(number_list)), number_list, color=colors)
plt.yticks(range(len(number_list)), labels)
plt.title('Cost of Hosting Summer Olympic Games')
plt.xlabel('Cost in Billions of dollar')
plt.ylabel('Cost')
plt.show()





#use input() to gain the correlated value of the cost of hosting the Summer Olympic Games in a list
#Convert the user input into a list of integers#sort the list
       #like 'costs=[1,8,15,7,5,14,43,40]'
       #the type of the input() is string , we will choose the number separated by commas
       #convert the string into a list 

# user_input = input("Enter a list of numbers separated by commas without blank like 'costs=[1,8,15,7,5,14,43,40]' : ")
#user_input = user_input[7:-1]
#number_list = [int(num) for num in user_input.split(',')]
