#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.


#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
while True:
    num_ply = int(input("the amount of players (has to be 2 or above) is: "))
    if num_ply >= 2:
        break

ply_rate_lis = []

for i in range(1,num_ply+1):
    while True:
        rating = int(input("the rating of player " + str(i) + " is : "))
        if 0 <= rating <= 5:
            break
    ply_rate_lis.append(rating)


print(ply_rate_lis)
print(sum(ply_rate_lis),"total")
print(sum(ply_rate_lis)/len(ply_rate_lis),"average")