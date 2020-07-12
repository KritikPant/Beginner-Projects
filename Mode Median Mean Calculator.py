data = []
print("\nFirst, we need to enter some numbers!")

#Data Collection
num=input("Type your first number: ")
while num:
    data.append(float(num))
    print("\n",data)
    num = input("Add another number, or press enter to move on.")

#Mean    
total = sum(data)
length = len(data)
print("\n\nThe Mean Is:",total/length)

#Median
data.sort()
x = length%2
half= length//2
if x == 1:
    print("The Median Is:",data[half])
else:
    low = int(data[half-1])
    high = int(data[half])
    print("The Median Is:",low+(high-low)/2)

#Mode
data2 = []
for item in data:
    tally = data.count(item)
    values = (tally, item)
    if values not in data2:
        data2.append(values)
data2.sort(reverse=True)
if data2[0][0]>data2[1][0]:
    print("\n\nThe mode is:", data2[0][1])
else:
    print("There is no mode")


    

