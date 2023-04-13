i=0
while i<=10:
    print(i+1)
    i+=1

# while(True):
#     print("ye chalta rahega")

while(True):
    num=int(input('enter the num'))
    print(num)
    if num==0:
        break
    else:
        continue

# letter generator

def letterGenerator(name,data):
    st = f'hi my name is {name}\n and i the biggest zero num {data}'
    print(st)
    #print(data)

letterGenerator('avi',1)

def average(a,b):
    return (a+b)/2
print(average(2,3))