start_range=int(input("Enter the start range: "))
end_range=int(input("Enter the end range: "))
l1=[]
for num in range(start_range, end_range + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            l1.append(num)
print(l1)