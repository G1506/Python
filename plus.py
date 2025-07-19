with open("file.txt", 'w') as f:
    f.write("Hello-students!!!!!!")
with open("file.txt", 'r+') as f:
    f.seek(0)
    data = f.read()
    print("Previous:", data)
    new_data = data.replace("students!!!!!!", "Future IT Employeeeeeeeee")
    
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("file.txt", 'r') as f:
    print("Latest:", f.read())
