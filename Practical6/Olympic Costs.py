#use input() to gain the correlated value of the cost of hosting the Summer Olympic Games in a list
#Convert the user input into a list of integers#sort the list
       #like 'costs=[1,8,15,7,5,14,43,40]'
       #the type of the input() is string , we will choose the number separated by commas
       #convert the string into a list 
#Sort the numbers in the list
#print the sorted list 

#draw the figure
# Set the custom colors and labels
# Create the bar plot
# Add color to bar
# Add the labels to the y-axis
# Add a title and labels to the x and y axes
# Add the x, y axin lables 
# Display the plot

user_input = input("Enter a list of numbers separated by commas without blank like 'costs=[1,8,15,7,5,14,43,40]' : ")
user_input = user_input[7:-1]
number_list = [int(num) for num in user_input.split(',')]
number_list.sort()
print("Sorted list: ", number_list)


import matplotlib.pyplot as plt         
colors = ['violet', 'indigo', 'blue', 'lime', 'green', 'yellow', 'orange', 'red']
labels = ['1', '2', '3', '4', '5', '6', '7', '8']
plt.barh(range(len(number_list)), number_list, color=colors)
plt.yticks(range(len(number_list)), labels)
plt.title('Cost of Hosting Summer Olympic Games')
plt.xlabel('Cost in Billions of dollar')
plt.ylabel('Cost')
plt.show()