# Defining the new function to add 2 numbers
def add(number1, number2):
    return number1 + number2

num1 = 4 # taking 1st variable value
num2 = 5 # taking 2nd variable value

total = add(num1, num2)  # passing the arguments to the function

print("The sum of {} and {} is {}".format(num1, num2, total))  #Displaying function