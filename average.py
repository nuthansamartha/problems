sum=0
for i in range(5):
    sum=sum+int(input(f"enter the marks of subject{i+1}: "))
average=sum/5
print(f"the average marks of the student is {average}")