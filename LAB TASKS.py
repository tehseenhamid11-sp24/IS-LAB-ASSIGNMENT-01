##LAB TASK NO 1

names_list = []
programs_list = []

noOfNames =  int(input("Element included in the names_list are: "))

for i in range(noOfNames):
    names = input("Enter the student names: ")
    names_list.append(names)

noOfPrograms = int(input("Element included in the Programs_list are: "))

for i in range(noOfPrograms):
    programs = input("enter the program names: ")   
    programs_list.append(programs)

merge_list = names_list + programs_list
print("the merged list is: " , merge_list)
merge_list.sort()
print("the sorted merged is: " , merge_list)



## LAB TASK 02


smallest = min(merge_list)
largest = max(merge_list)
print("the smallest element (no.of characters) of the merged list is: ", smallest)
print("the largest element (no.of characters) of the merged list is: ", largest)


##LAB TASK 03

birthday_dict = {
    "Tehseen Hamid": "11/08/2003",
    "Yumna Tehseen": "21/11/2003",
    "Gul Wali Khan": "12/10/1995"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthday_dict:
    print(name)

name = input("Who's birthday do you want to look up? ")

if name in birthday_dict:
    print("{name}'s birthday is on {birthday_dict[name]}.")
else:
    print("Sorry, we don't have that person's birthday.")
    
    
    
    
##LAB TASK 04

original_dict = {
    "Name": "Tehseen",
    "Age": 22,
    "City": "Swat",
    "Job": "Software Engineer"
}

keys_to_extract = ["name", "job"]
new_dict = {}
for key in keys_to_extract:
    if key in original_dict:
        new_dict[key] = original_dict[key]

print("New dictionary:", new_dict)





























