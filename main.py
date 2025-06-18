# info = {"name": "Alex", "age": 25}
# info["city"] = "New York"
# print(info['city'])

# contacts = {}

# while True:
#     print("\n1. Add Contact\n2. View All\n3. Search\n4. Delete\n5. Exit")
#     choice = input("Enter choice: ")
    
#     if choice == '1':
#         name = input("Name")
#         phone = input("Phone")
#         contacts[name] = phone
#         print('Contact Saved!')
        
#     elif choice == '2':
#         for name,phone in contacts.items():
#             print(f"{name}:{phone}")
#     elif choice == '3':
#         name = input("Enter name to search:")
#         if name in contacts:
#             print(f"{name}'s phone:{contacts[name]}")
#         else :
#             print("not Found!")
#     elif choice == '4':
#          name = input("Enter name to delete: ")
#          if name in contacts:
#             del contacts[name]
#             print("Deleted successfully.")
#          else:
#             print("No such contact.")
#     elif choice == '5':
#         break
#     else:
#         print("Invalid choice.")
        
        
 
# student = {
#     "name": "Amit",
#     "age": 21,
#     "course": "Python"
# }  

# print(student.get('name'))    
# print(student.keys())    
# print(student.values())  
# print(student.items())  
           
# student["grade"] = "A+"  
# print(student.keys())    

# grocery_list = []

# while True:
#     print("\nOptions: add / remove / show / exit")
#     action = input("What would you like to do? ")

#     if action == "add":
#         item = input("Enter item to add: ")
#         grocery_list.append(item)
#         print(f"{item} added.")
    
#     elif action == "remove":
#         item = input("Enter item to remove: ")
#         if item in grocery_list:
#             grocery_list.remove(item)
#             print(f"{item} removed.")
#         else:
#             print("Item not found.")
    
#     elif action == "show":
#         if(len(grocery_list) != 0):
#             print("Your grocery list:")
#             for i in grocery_list:
#               print("-", i)
#         else:
#             print('groccy list is empty nothing here')
                  
    
#     elif action == "exit":
#         break

#     else:
#         print("Invalid option.")


# set are remove automatically duplicate values
# ids = {1,2,2,3,3,4,4,4,5}
# print(ids)


# tuple
colors = "red", "green", "blue"
colors = ("red", "green", "blue")
print(colors[0]) 
print(len(colors)) 


students = { 'name': 'Zulkaif',
            "age" :23,
            "subjects" : ["Eng","phy","urdu"],
            "Marks" : {"Eng": 76,"phy":98,"urdu":34}
            }

print(students)
# print(students.keys())    
# print(students.values())  
# print(students.items())

for sub,val in students["Marks"].items():
    print(f"{students["name"]} and subjects Marks {sub}-{val}")