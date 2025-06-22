import os
import datetime

def check_space(command):
    print(os.system(command))
    
def show_date():
    return datetime.datetime.today()

check_space('df -h')
today = show_date()
print(today)




