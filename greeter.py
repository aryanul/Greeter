# https://docs.python.org/3/library/time.html#time.strftime
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
minute = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))
if hour>=4 and hour<12:
    print("Good Morning !")
elif hour>=12 and hour<17:
    print("Good Afternoon !")
elif hour>=17 and hour<21:
    print("Good Evening !")
else:
    print("Good Night !")