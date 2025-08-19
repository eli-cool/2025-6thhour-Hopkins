#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: HW2


#1. Print "Hello World!"
print("hi")
#2. Create three different variables with distinct names and values: one with an integer, one with a string, one with a boolean.
var_1 : int = 10
var_2 = "var"
var_3 : bool = True
#3. Print all three variables on the same print function (at the same time).
print(var_1, var_2, var_3)
#4. Create a variable that asks the user to input an integer.
var_ask = int(input("Enter a number: "))
#5. Add the integer variable from #2 with the integer from #4 and print the result.
var_2_2 = var_1 +var_ask
print(var_2_2)
#6. Take the result from #5 and divide it by 2. Print the result.
print(var_2_2 / 2)
#7. Change the value of the boolean variable to the opposite value (if true then make false, or vice versa).
var_3 = not var_3
#8. Print the value of the boolean variable.
print(var_3)
#9. Create a variable with a number that contains decimals.
var_dec = 1.414213562373095048
#10. Round the number from #9 up or down using the round function.
print(var_dec.__ceil__())