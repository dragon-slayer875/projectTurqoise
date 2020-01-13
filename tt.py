import random
import tkinter as tk

#layout

#functions
def input_int():
    while True:
        args=input()
        if args.isnumeric()==True:
            args=int(args)
            break
        else:
            print('Not a number. Try again')
            continue
    return args

def input_name():
    while True:
        args=input()
        if args.isalpha()==True:
            args=args
            break
        else:
            print('Not a name. Try again')
            continue
    return args

#declarations
main=[]
main1=[]
subjects=[]
tsub=0
m=[]
l=[]

#data
print('Enter the number of subjects you want:')
n=input_int()

print('Enter the number of days the school is open:')
iday=input_int()

print('Enter the number of periods in a day:')
iperiod=input_int()

for i in range(n):
    print('Enter the name of the subject:')
    sub=input_name()

    print('Enter the number of times you want it:')
    rep=input_int()

    tsub+=rep
    subjects.append(sub)

    for j in range(rep):
        main.append(sub)
        
#working            
for z in range(5):
    main1.extend(main)
    if tsub>iday*iperiod:
        print('Number of periods are out of range.Try again.')
        
    else:
        m=[]
        l=[]

        for i in range(iday):
            for j in range(iperiod):
                x=random.choice(main1)
                l.append(x)
                main1.remove(x)
            for k in l:
                if l.count(k)>2:
                    l.remove(k)
                    main1.append(k)
                    x=random.choice(main1)
                    l.append(x)
                    main1.remove(x)
            m.append(l)
            l=[]

        r=len(m)
        c=len(m[0])
        for i in range(r):
            for j in range(c):
                print('%10s'%(m[i][j]),end='')
            print()
        print()
        print()
