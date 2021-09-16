#write a Python program to display the current date and time
import datetime
#for i in dir(datetime):
  # print(i)


currenttime = datetime.datetime.now()
print("Current date and time : ")
print(currenttime.strftime("%y-%m-%d %H:%M:%S %D %A"))
