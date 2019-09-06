students={'1MS16IS100':'Asha', '1MS16IS101':'Ashok', '1MS16IS102':'Rekha', '1MS16IS103':'Suma'}
list=["value1","value2","value3","value4"]
list2=[]
j=0
for i in students:

	print("key is",i,"value is",students[i])
	list[j]=students[i]
	j=j+1

print(list)
print(students.keys())
print(students.values())
print(students.items())
