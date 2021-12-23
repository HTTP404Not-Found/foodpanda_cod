import time 
def adjust (unm):
    if unm < 10 :
        unm = "0" + str(unm)
    return unm

time = time.localtime(time.time())
year = time.tm_year
mon = time.tm_mon
day = time.tm_mday
hour = input("hour?=" ) 
min = input ("min?=")
pr_1 = str(adjust(day)) + str(adjust(mon)) + str(adjust(year))
pr_2 = str(hour) + str(min)
print(pr_1 + " " + pr_2)
input("    ")