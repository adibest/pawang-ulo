with open("biodata.txt","r") as file:
    file = file.read()
    print (file[3:14])
    for i in file:
        if i == '.':
            break
        print (i)