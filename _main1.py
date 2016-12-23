import datetime
import random
import time
import matplotlib.pyplot as plt
from dateutil import parser

# make up some data
x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
y = [i+random.gauss(0,1) for i,_ in enumerate(x)]

x = datetime.datetime.strptime('18:19:23.232415'.split('.')[0],'%H:%M:%S')

x1 = [x + datetime.timedelta(seconds=i) for i in range(12)]

#print x1
print (x)


# plot
plt.plot(x1,y)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()