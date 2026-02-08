####### Question-1 #######

# with open('names.txt','w+') as f:
#     for i in range(1,6):
#         name=input(f"Enter {i} names :")
#         f.writelines(f"{name}\n")

# with open('names.txt','r') as f:
#     names=f.read()
#     print(names)

#### Simple way

# with open('names.txt', 'w') as f:
#     f.writelines(input(f"Enter {i} name : ") + "\n"
#         for i in range(1, 6))

# print(open('names.txt').read())



####### Question-2 #######

# with open("log.txt", "a") as f:
#         f.write("Program run successfully\n")

# with open("log.txt", "r") as f:
#     print(f.read())


####### Question-3 #######

# l= [5, 10, 15, 20, 25]

# new_list=[i  for i in l if i >15]
# print(new_list)


####### Question-4 #######


# import json
#  # 1. Create dictionary of 3 cities and save to JSON
# cities = {
#         "Delhi": 19000000,
#         "Mumbai": 21000000,
#         "Kolkata": 15000000
# }

# with open("cities.json","w") as f:
#     json.dump(cities,f,indent=4)


#    # 2. Load the JSON file and print each city with population
# print("\nCurrent Cities and Populations:")
# with open("cities.json", "r") as f:
#     data = json.load(f)
#     for city, population in data.items():
#         print(f"{city} : {population}")

# # 3. Ask user to add new city + population
# new_city = input("\nEnter new city name: ")
# new_population = int(input("Enter its population: "))

# # Update dictionary
# data[new_city] = new_population

# # Save updated data back to JSON
# with open("cities.json", "w") as f:
#     json.dump(data, f, indent=4)

# print("\nUpdated JSON saved successfully!")

# print("\nCurrent Cities and Populations:")
# with open("cities.json", "r") as f:
#     data = json.load(f)
#     for city, population in data.items():
#         print(f"{city} : {population}")


####### Question-5 #######

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")