with open("log.txt",'a+') as f:
    f.write("Bravoo!15t06")
    f.seek(0)
    data=f.read()
    print("current data:\n",data)