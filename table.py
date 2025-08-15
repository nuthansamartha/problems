start_range=int(input("Enter the start range: "))
end_range=int(input("Enter the end range: "))
l1=[]
for i in range(start_range, end_range + 1,6):
    if i % 2 == 0:
        l1.append(i)
print(l1)