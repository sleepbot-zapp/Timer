import time

def countdown(itime):
   while itime >= 0:
      mins, secs = divmod(itime, 60)
      if mins < 60:
         timer = '{:02d}:{:02d}'.format(mins, secs)
      else:
         hours, mins = divmod(mins, 60)
         timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
      print(timer, end='\r')
      time.sleep(1)
      itime -= 1

if __name__ == '__main__':
   itime = int(input("Enter a time in seconds: "))
   countdown(itime)
