import random as R
import time as T
points=pow(1000,2)
ypoints=0.0
start = T.perf_counter()
for i in range(1,points):
    x,y =R.random(),R.random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        ypoints+=1
pi =4*(ypoints/points)
print("圆周率为：{}".format(pi))
print("圆形时间为：{:.5f}s".format(T.perf_counter()-start))
