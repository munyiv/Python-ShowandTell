Audrey={'name':'Audrey','age':19,'country':'Kenya','county':'Machakos'} #dictionary
student=[Audrey]#Changed the value of Audrey  to Student
print (student)# output the value of student
for student in student: 
    name=student['name']
    age=student['age']
    county=student['county']
    sentence="{} is {} years and is from {} county".format(name,age,county)
    print(sentence)# to get an output
    x=("Nairobi","Kisumu","Mombasa","Kitui")#tuple
    for a in x: 
            print(a)# getting the values of x printed in a new line
            

    
            

    
    
    

    
