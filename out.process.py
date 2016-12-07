import sys

flag = False
for line in sys.stdin:
    if flag:
        print line[:-1]+" 1"
    if line.startswith(" *** LIST OF UNPACKED BOXES ***"):
        flag=True
        print "12033, 2350, 2394"
