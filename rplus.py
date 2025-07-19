with open("file.txt",'w') as f:
    f.write("Sai Krishna")
with open ("file.txt",'r+') as f:
    data=f.read()
    new_data =data.replace("sai","bava")
    f.seek(0)
    f.write(new_data)
    f.truncate(3)
with open("file.txt",'r') as f:
    print("Latest:",f.read())