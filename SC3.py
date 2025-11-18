#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

import random
#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
while True:
    num_ply = int(input("the amount of players (has to be 2 or above) is: "))
    if num_ply >= 2:
        break

ply_rate_lis = []
clothes_rate_lis = []

for i in range(1,num_ply+1):

    rancol = ["red", "blue", "green", "yellow", "purple", "pink"]
    cloth_color = random.choice(rancol)
    print("player", str(i), "their outfit is", cloth_color)

    #rating loop
    while True:
        rating = int(input("rate the "+cloth_color+" outfit of player " + str(i) + "from 1 to 5: "))
        if 0 <= rating <= 5:
            break
    ply_rate_lis.append(rating)
    clothes_rate_lis.append(cloth_color)



print(ply_rate_lis)
print(clothes_rate_lis)
print(sum(ply_rate_lis),"total")
print(sum(ply_rate_lis)/len(ply_rate_lis),"average")


highest = max(ply_rate_lis)
highest_index = ply_rate_lis.index(highest)
print("the highest rating is player", highest_index + 1,"with a", clothes_rate_lis[highest_index],"colored outfit.")