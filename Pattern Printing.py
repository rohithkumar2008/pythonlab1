print("Enter the Diamond height") 
choice=int(input()) 
for x in range(choice):
    print(' '*(choice-x-1),'*'*(2*x+1)) 
for y in range(choice-2,-1,-1):
    print(' '*(choice-1-y),'*'*(2*y+1)) 
