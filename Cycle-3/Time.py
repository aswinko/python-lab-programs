class Time:
    def __init__(self, hr, mt, sec):
        self.hr = hr
        self.mt = mt
        self.sec = sec
    def __add__(self, x):
        sum1 = self.hr + x.hr
        sum2 = self.mt + x.mt
        sum3 = self.sec + x.sec
        if sum3 >= 60:
            sum3 -= 60
            sum2 += 1
        if sum2 >= 60:
            sum2 -= 60
            sum1 += 1
        print(sum1, " ", sum2, " ", sum3)
print("Time 1")
hr = int(input("Enter hour : "))
mt = int(input("Enter minute : "))
sec = int(input("Enter second : "))

time1 = Time(hr, mt, sec)

print("Time 2")
hr = int(input("Enter hour : "))
mt = int(input("Enter minute : "))
sec = int(input("Enter second : "))

time2= Time(hr, mt, sec)

time1 + time2
