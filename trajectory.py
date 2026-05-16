#now we want to see the trajectory of masses on a pendulum
import matplotlib.pyplot as plt
from simulation import x1, y1, x2, y2, th

#plotting y(x) dependencies
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
