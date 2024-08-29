dict_main={}
a=int(input("enter the number of students to add"))

for x in range(0,a):
    dict_stu={}
    dict_stu["name"]=input("Enter name of student")
    dict_stu["class"]=input("Enter class of student")
    dict_stu["height"]=input("Enter height of studentin cm")
    dict_stu["weight"]=input("Enter nweight of student")
    dict_stu["sport"]=input("Enter interested sport")
    dict_stu["calorie"]=input("Enter calorie intake")
    dict_main[dict_stu["name"]]=dict_stu
    
b=input("Enter name of student to calculate chart")

dict_stu=dict_main[b]
weight=int(dict_stu["weight"])
height=int(dict_stu["height"])
calorie=int(dict_stu["calorie"])


halfbmi=height/weight

if height>180 and weight<70:
    print("red")
elif height<180 and weight >80 and calorie>2000:
    print("orange")
elif height<180 and weight >90 and calorie<=2000:
    print("green")
elif halfbmi>2:
    print("red")
elif halfbmi<=2:
    print("green")
