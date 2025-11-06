def checkodd(inputf,outputf):
    with open(inputf,'r')as infile:
        lines=infile.readlines()
    with open(outputf,'w')as outfile:
        length=len(lines)
        for x in range(length):
            if(x%2==0):
                outfile.write(lines[x]) 
inputfile="D:\\Bcs\\check.txt" 
outputfile="D:\\Bcs\\pythonodd.txt" 
checkodd(inputfile,outputfile)
