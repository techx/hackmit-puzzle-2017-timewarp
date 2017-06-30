import hashlib
import struct
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta

from config import SECRET

BASE_DT = DateTime(1, 1, 1)

def u_to_i(u):
    m = hashlib.sha256((SECRET + u).encode('utf-8'))
    d = m.digest()
    i = struct.unpack('<B', d[0:1])[0]
    return i

def u_to_date(u):
    i = u_to_i(u)
    return date_for_i(i)

def date_for_i(i):
    t = BASE_DT + TimeDelta(days=i*1000, hours=(i%60), minutes=((i*3)%60))
    return t.strftime('%b %d %Y %I:%M %p')

def file_for_u(u):
    i = u_to_i(u)
    print(i)
    return file_for_i(i)

def file_for_i(i):
    return hashlib.sha256((SECRET + str(i)).encode('utf-8')).hexdigest() + '.class'
