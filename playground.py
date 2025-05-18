import datetime
import random
# print(datetime.datetime(year = 1996,month=4, day=1))
print(random.choices(['activo', 'licencia','inactivo'], weights=[20, 5, 2], k=1))