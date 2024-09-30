# Cooper Stolebarger
# UWYO COSC 1010
# Submission Date: 09/26/2024
# Lab 03 
# Lab Section: 
# Sources, people worked with, help given to: Lecture slides and TA


# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
States = ["Wyoming", "Colorado", "Montana"]
print(States)
print(States[0])
print(States[-1])
print(f"{States[1].upper()} is south of {States[0].upper()}")


print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
States.append("Washington")
States.append("Oregon")
States.append("California")
print(States)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
States[-2] = "Maine"
print(States)

#Insert the state Texas to be the third element in the list, again printing your list
States[2] = "Texas"
print(States)

#Using the `del` statement remove the fourth item from the list, print your list 
del States[3]
print(States)

States.remove("Texas")
print(States)


print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
sorted_states = sorted(States)
print("Sorted list:", sorted_states)
print("Unsorted list:", States)

States.sort(reverse=True)
print(States)

States.reverse()
print(States)
