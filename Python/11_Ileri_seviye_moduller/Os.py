import os
import datetime
result=os.stat("datetime.py")
result=datetime.datetime.fromtimestamp(result.st_ctime)

print(result)