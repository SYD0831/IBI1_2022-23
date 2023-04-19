# define a function called is _afford () to get the result
# input two values and get the maxium value of the house
# compare the home_value and maxium value
# return Yes/No
def is_afford (salary, home_value):
    """
	Input: salary, home_value
	Returns Yes if the purchaser can buy the house, otherwise No
	"""
    Maximum_value = salary*5
    if home_value > Maximum_value:
        return "No"
    elif home_value <= Maximum_value:
        return "Yes"

# Example usage
#you can change the salary and the house value here
salary = 3000
home_value = 180000
result = is_afford (salary, home_value)
print(result)

