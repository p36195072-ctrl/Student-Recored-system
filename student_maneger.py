student = {}
while True:
    print("=== IF U WANT TO EXIT WRITE 'EXIT' === ")
    name = input("Enter your student name:")
    name = name.strip()

    if name.lower() == "exit":
        break

    if name.strip() == "":
        print("Cannot be empty")
        continue

    age = input("Enter the students age:").strip()
    

    if age.strip() == "":

    
        print("Cannot be empty")
        continue

    student[name] = {
        "age":age
    }

    city = input("Enter the city your live:")
    if city.strip() == "":
        print("City can't be empty")
        continue
    
    if city.strip() == " ":
        print("City can't be empty")
        continue
    student[name] = {
        "age" : age,
        "city" : city
    }


    classe = input("Enter your class:").strip()
    if classe == "":
        print("Class can't be empty")
        continue

    classes = int(classe)

    student[name] = {
        "age" : age,
        "city" : city,
        "classes" :classes
    }
        
    search = input("Search student: ").strip()
    if search == "":
        print("It cannt be empty")
        continue

    if search in student:
        print(student[search])
    else:
        print("Not Found")

    student[name] = {
        "age":age,
        "city" : city,
        "classes" : classes,
        "search " : search

    }

  
    
    print(student)
    print ("done")
    print("Total number of students:", len(student))
    

    