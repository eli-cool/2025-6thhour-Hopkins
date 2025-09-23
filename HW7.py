#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print("hello world")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
numd = {
    "dic1":1,
    "dic2":"sonic",
    "dic3":[1,2,3],
}
#3. Print the keys of the dictionary from #2.
print(numd.keys())
#4. Print the values of the dictionary from #2
print(numd.values())
#5. Print one of the three numbers from the list by itself
print(numd["dic3"][2])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
numd.update({"dic4":"hi"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(numd)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
classroom= {
    "student1":
        {
            "name":"Ally",
            "age":"17",
            "favorite":"purple",
        },
    "student2":
        {
            "name":"Alaia",
            "age":"14",
            "favorite":"lilac",
        },
    "student3":
        {
            "name":"Brodie",
            "age":"16",
            "favorite":"purple",
        }


}
#9. Print the names of all three classmates on the same line.

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.