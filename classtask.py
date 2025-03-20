

data={}
qualification={}
listdata=[]
list=[]
data["studentid"]=int(input("please enter the student id"  ))
data["studentname"]=input("please enter the student name")
data["experinces"]=input("please enter the experince")
data["skills"]=input("please input the student skills")

qualification["name"]=input("please input quallification name")
qualification["passingyear"]=input("please enter passing year")

listdata.append(qualification)
qualification={}
qualification["name"]=input("please input quallification name")
qualification["passingyear"]=input("please enter passing year")
listdata.append(qualification)
data["qualifications"]=listdata

list.append(data)
data1={}
qualification={}
listdata=[]
data1["studentid"]=int(input("please enter the student id"  ))
data1["studentname"]=input("please enter the student name")
data1["experinces"]=input("please enter the experince")
data1["skills"]=input("please input the student skills")

qualification["name"]=input("please input quallification name")
qualification["passingyear"]=input("please enter passing year")

listdata.append(qualification)
qualification={}
qualification["name"]=input("please input quallification name")
qualification["passingyear"]=input("please enter passing year")
listdata.append(qualification)
data1["qualifications"]=listdata
list.append(data1)




print(list)






 









