num=[12,4,56,39,34,22,77,17,47] 
evencount=0 
oddcount=0 
for x in num:
    if(x%2==0):
        evencount+=1
    else:
        oddcount+=1 
print("Total Even Numbers count:",evencount) 
print("Total Odd Numbers count:",oddcount)
