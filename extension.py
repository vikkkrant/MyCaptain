file_name = input("Enter the name of file to display type of file : ")
ext = file_name.split(".")
if ext[1]=="py":
    print("It is a python file")
elif ext[1]=="cpp":
    print("It is a C++ file")
elif ext[1]=="mp3":
    print("It is a audio file")
elif ext[1]=="jpg":
    print("It is a image file")
elif ext[1]=="php":
    print("It is a php file")
elif ext[1]=="java":
    print("It is a java file")
elif ext[1]=="pdf":
    print("It is a pdf file")
elif ext[1]=="ppt":
    print("It is a ppt file")
elif ext[1]=="html":
    print("It is a html file")
elif ext[1]=="class":
    print("It is a java class file")
elif ext[1]=="cs":
    print("It is a visual C# source code file")
elif ext[1]=="swift":
    print("It is a Swift source code file")
elif ext[1]=="sh":
    print("It is a Bash shell file")
elif ext[1]=="vb":
    print("It is a visual basic file")
else:
    print("Not recognised")
