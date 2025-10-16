def hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from rod",source, "to rod",target)
        return
    hanoi(n - 1, source, auxiliary, target)
    print("Move disk",n,"from rod",source, "to rod",target)
    hanoi(n - 1, auxiliary, target, source) 
input_disk=int(input("enter number of disks ")) 
num_disks =input_disk 
hanoi(num_disks, 'A', 'C', 'B')
