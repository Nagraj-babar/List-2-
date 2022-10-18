# Write a Python script to create a list of first N even natural numbers.
a=int(input("Enter a Number: "))
r=range(1,a+1)
x=[]
for e in r:
    if e%2==0:
        x.append(e)
print(x)        
