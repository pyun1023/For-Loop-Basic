for i in range(0,151):
    print(i)

for i in range(1,201):
    print(i*5)


for i in range(1,101):
    if i % 10 == 0:
        print('Coding Dojo')
    else:
        print(i)
    if i % 5 == 0 and i %10!=0:
        print ('Coding')
    
sum=0
for i in range(0,500001):
    if i%2==1:
        sum+=i
print(sum)

for i in range(2018,0,-4):
    print(i)


lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum,highNum + 1):
    if i % mult == 0:
            print(i)

