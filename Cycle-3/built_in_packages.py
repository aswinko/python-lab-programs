import statistics, math, time

print("The vaue of pi is : ", math.pi)
print("Seconds since epoch = ", time.time())
li = [1, 2, 3, 3, 2, 2, 2]
print("The average of list values is ", statistics.mean(li))
print("Local time : ", time.ctime(time.time()))

