import time
a=0

x=time.perf_counter()
while (a<10000):
    print(a)
    a+=1 

y=time.perf_counter()
print(y-x)