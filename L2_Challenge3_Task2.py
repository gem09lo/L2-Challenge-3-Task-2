#python L2_Challenge3_Task2.py
#Task 2 - HR Management System

##MAKING A LIST OF DICTIONARIES
people = []
d1 = {"name": "Jane Doe", "age": 42, "employed": "Yes"}
d2 = {"name": "Tom Smith", "age": 18, "employed": "Yes"}
d3 = {"name": "Mariam Coulter", "age": 66, "employed": "No"}
d4 = {"name": "Gregory Tims", "age": 8, "employed": "No"}
people.append(d1)
people.append(d2)
people.append(d3)
people.append(d4)

##FORMAT SO PEOPLE DICT IS READABLE
def display_dict(people):
    for person in people:
        for key, value in person.items():
            print("{}: {}".format(key.title(), value))
display_dict(people)

"""Functions for adding or removing users"""
def adding_user():
    add_dict = {}
    first_name, last_name, age, employed = (input("Enter your full name, age and whether you are employed or not (with space in between): ")).split()
    add_dict["name"] = "{} {}".format(first_name.title(), last_name.title())
    add_dict["age"] = age
    add_dict["employed"] = employed.title()
    people.append(add_dict)

def removing_user():
    name_input = (input("Enter the name you want to remove: ")).title()
    for person in people:
        if name_input in person["name"]:
            people.remove(person)

"""Function that askes user if they want to add or remove users"""
def add_or_remove(people):
    prompt = input("Do you want to add or remove? ").title()
    if prompt == "Add":
        adding_user()
    elif prompt == "Remove":
        removing_user()

while True:
    add_or_remove(people)
    display_dict(people)



##FUNCTION FOR ADDING OR REMOVING USERS
#def add_or_remove():
    #prompt = input("Do you want to add or remove? ").title()
    #if prompt == "Add":
        #add_dict = {}
        #first_name, last_name, age, employed = (input("Enter your full name, age and whether you are employed or not (with space in between): ")).split()
        #add_dict["name"] = "{} {}".format(first_name.title(), last_name.title())
        #add_dict["age"] = age
        #add_dict["employed"] = employed.title()
        #people.append(add_dict)
    #elif prompt == "Remove":
        #name_input = (input("Enter the name you want to remove: ")).title()
        #for person in people:
            #if name_input in person["name"]:
                #people.remove(person)

#print(add_or_remove())

#for person in people:
    #for key, value in person.items():
        #print("{}: {}".format(key.title(), value))
