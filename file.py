print("---Student Managent System---")
print("1.Write Student")
print("2.Display Student")
print("3.Search Student")
print("4.Count Student")
print("5.Exit")
option=int(input("Enter an Option: "))
if option==1:
    n=int(input("Enter Number of Students: "))
    with open("student.txt","w") as f:
        for i in range(n):
            print(f"Enter Student Details: {i+1}")
            rollno=input("Enter Rollno: ")
            name=input("Enter Name: ")
            course=input("Enter Course: ")
            fee=input("Enter Fee: ")
            f.write(rollno + "," + name + "," + course + "," + fee + "\n")
    print("Student added Successfully")
elif option==2:
    with open("student.txt","r") as f:
        data=f.read()
        print(data)
elif option==3:
    name=input("Enter Name to search: ")
    with open("student.txt","r") as f:
        n=False
        for line in f:
            if name in line:
                print("Student Found")
                print(line)
                n=True
        if n==False:
            print("Student Not Found")
elif option==4:
    count=0
    with open("student.txt","r") as f:
        for line in f:
            count+=1
    print("Total Students: ",count)
elif option==5:
    print("Exit,Thank You")
else:
    print("Invalid Option")