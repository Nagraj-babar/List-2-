# Write a Python script to remove all non int values from a list.
l1=[20,30,True,'Nagraj',40,50,4.5]
l2=[]
for e in l1:
    x=type(e)
    if x==int:
        l2.append(e)
print(l2)        