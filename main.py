def bubble(a):
    for i in range(0,len(a)-1):
        for m in range(len(a)-1):
            if(a[m]>a[m+1]):
                a[m],a[m+1] = a[m+1], a[m]
    return a
import random
a = []
for i in range(10):
    a.append(random.randint(1,100))
print(a)
print(bubble(a))