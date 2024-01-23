#student = ["Jessica", "Charles", "jordan", "Ralph"]
#print(student[1])
#print(len (student)) len is for total number 
#print(student[1:3]) doesnt include the 3rd one
#print(student[1:]) : include things after 1 
#print(student[:3])
#print(student[0:])

#student = ["Jessica", "Charles", "jordan", "Ralph"]
#print (list(student))
date = "2024/01/20"
#print(date.split("/")) /to split 
#print("/".join(student))  use / symbol to join together
#student[1]= "Vera" to replace one of numbers in the list
#print(student)
# if do not want the original list to be changed, change [] into ()
#student = ("Jessica", "Charles", "jordan", "Ralph") to be locked of this ()

student = ["Jessica", "Charles", "jordan", "Ralph"]
#student.append("Charles") only to add one 
#student .extend(["charles", "zheng"]) extend is to add more than one, use [""]
#student.remove("jordan") to remove from the list
#student.pop(1) to remove by the order number 
#print(student)
#print("vera"in student) use in to check if vera was in the list.
#if "vera" in student:
#    print("vera is on the list.")
#else:
#    print("vera is not on the list.")
#print(student.index("Charles")) to find out the order of charles 

grades_system= ["jessica", 100, "charles", 88, "jordan", 30, "vera", 99]
modify= input("please enter what you want to do(A)search (B)add (C)delete (D)change:").upper()
if modify == "A":
    name = input("please enter the name you want to search:")
    if name not in grades_system:
        print("this person does not exist.")
    else:
        order = grades_system.index(name)
        print(f"the grade of {name} is {grades_system[order+1]}.") #+1 meaning grade after the name
elif modify == "B":
    student_profile = input("please enter the name/grade you want to add (use/to split it):")
    grades_system.extend(student_profile.split("/"))
    print("grade added succussfully.")
    print(f"currently the number of students online is {int(len(grades_system)/2)}.")
elif modify == "C":
    name = input("please enter the name and grade you want to delete:")
    name_position= grades_system.index(name)
    grades_system.pop(name_position)
    grades_system.pop(name_position)
    print("name deleted.")
    print(grades_system)
elif modify == "D":
    name = input("please enter the name:")
    grade = input ("the grade is :")
    name_position= grades_system.index(name)
    grades_system[name_position+1] = grade
    print(grades_system)