#Discussion on Loops
#There are 2 type of loop in python - For loop and While loop

#For loop
#For <variable> in <list of values>:
#     step 1
#     step 2
#a range function will create list of values for you.

for i in range(1,987):
	print(i)
	#Do this

#Can i only use numbers? No , any thing that's in list
listOfNames = ['Avi','Ranvir', 'Suhas', 'Shiv']
for name in listOfNames:
	print("Attending Class ",name)

# A few more intresting things.
# Printing squares ( number * number) for numbers from 1 to 6543

print("printing squares from 1 to 876")
for i in range(1,877):
	print(i*i, end=" ")

#While Loop - Just a diffirent way to do a loop
# while(Condition is True):
#          steps

print("printing squares from 1 to 876")
i = 1
while(i<877):
	print(i*i, end=" ")
	i = i +1
	
#Class practice problem
#Print Cube of a numbers from 1 to 654
#Cube is a number multipled thrice by itself. i*i*i










