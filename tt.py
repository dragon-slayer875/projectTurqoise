import random
import string
q=string.ascii_letters
r=string.punctuation
n1=input('Enter the number of subjects you want:\n')

while(n1=="" or n1 in q or n1 in r):
    print("Try again")
    n1=input("Enter\n")
else:
    n=int(n1)
main=[]
main1=[]
subjects=[]
tsub=0
iday1=input('Enter the number of days the school is open:\n')
while(iday1=="" or iday1 in q or iday1 in r):
    print("Try again")
    iday1=input("Enter\n")
else:
    iday=int(iday1)
iperiod1=input('Enter the number of periods in a day\n')
while(iperiod1=="" or iperiod1 in q or iperiod1 in r):
    print("Try again")
    iperiod1=input("Enter\n")
else:
    iperiod=int(iperiod1)


for i in range(n):
    sub=input('Enter the name of the subject:\n')
    rep=int(input('Enter the number of times you want it:\n'))
    tsub+=rep
    subjects.append(sub)
    for j in range(rep):
            main.append(sub)
            main1.append(sub)
            
for z in range(5):
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

        main1.extend(main)
        r=len(m)
        c=len(m[0])
        for i in range(r):
            for j in range(c):
                print('%10s'%(m[i][j]),end='')
            print()
        print()
        print()
    m=[]
    
