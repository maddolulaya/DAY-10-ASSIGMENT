
department=input("enter your department (cse,ece,mech,civil): ")
if department=="cse":
    print("welcome to the cse department")
    position=input("are you faculty or student?: ")

    if position=="faculty":
        print("welcome sir go to staff room")
    elif position=="student":
        print("welcome go to class room")
    else:
        print("invalid position in depatment")

elif department=="ece":
    print("welcome to the ece department")
    position=input("are you faculty or student?: ")

    if position=="faculty":
        print("welcome sir go to staff room")
    elif position=="student":
        print("welcome go to class room")
    else:
        print("invalid position in department")

elif department=="mech":
    print("welcome to the mech department")
    position=input("are you faculty or student? : ")

    if position=="faculty":
        print("welcome sir go to staff room ")
    elif position=="student":
        print("welcome go to class room")
    else:
        print("invalid position in department")

elif department=="civil":
    print("welcome to the civil department")
    position=input("are you faculty or student?: ")
    
    if position=="faculty":
        print("welcome sir go to staff room")
    elif position=="student":
        print("welcome go to class room")
    else:
        print("invalid position in department")

else:
    print("inavlid department")