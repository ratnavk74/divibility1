start= int(input("Enter starting number:"))
end= int(input("Enter ending number:"))

print(f"Numbers divisible by 5 between {start} and {end}")
for i in range(start,end+1):
    if i % 5 == 0:
        print(i)


