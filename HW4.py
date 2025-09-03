#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: HW4


#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
lis=["scout","soldier","pyro","heavy","demo"]
#2. Append a new name onto the Name List.
lis.append("engineer")
#3. Print out the 4th name on the list.
print(lis[3])
#4. Create a list with 4 different integers in it.
numlis=[4,5,6,7]
#5. Insert a new integer into the 2nd spot and print the new list.
numlis.insert(1,3)
#6. Sort the list from lowest to highest and print the sorted list.
numlis.sort()
print(numlis)
#7. Add the 1st three numbers on the sorted list together and print the sum.
newnumlis=numlis[:3]
print(sum(newnumlis))
#8. Create a list with two strings, two variables, and too boolean values.
multi=[6,7,"sniper","medic",True,False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(multi[int(input())])