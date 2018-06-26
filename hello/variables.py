tuple=('rahul',100,60.4,'deepak')
tuple1=('sanjay',10)
print(tuple1)
print(tuple[2:])
print(tuple+tuple1 )
dictionary={'name':'charlie','id':100,'dept':'it'}
print(dictionary )
list=['sanjota',678,20.4,'saurav']
print(list)
print(list[0:4])
print(list*2 )
a=70
b=20
list=[10,20,30,40,50];
if (a in list):
    print ("a is in given list")
else:
    print ("a is not in given list")
if(b not in list):
    print ("b is not given in list")
else:
    print ("b is given in list")
    a = 20
    b = 20
    if (a is b):
        print("a, b have same identity")

    else:
        print("a,b are different")

    b = 10
    if (a is not b):
        print("a,b have different identity")

    else:
        print("a, b have same identity")
num = 2
for a in range (1,6):
    print(num * a)
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(i,)
        print