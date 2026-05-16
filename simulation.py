#this file contains only simulation of motion, solving equations and plots angle(time)
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#parameters of the system
g = 9.81
m1 = 1
m2 = 1
l1 = 1
l2 = 1

#initial conditions
S0 = [np.pi/2, 0, np.pi/2, 0]
#timespan for solving
ts = np.linspace(0,10,1000)

#derivative of the state vector
def dotS(t, S):
    theta1, omega1, theta2, omega2 = S
    
    #we define new variables like diffrence of angles and common denominator to write the formula easier
    delta = theta1 - theta2
    den = 2*m1 + m2 - m2*np.cos(2*delta)

    #calculating angular accelerations
    alpha1 = (-g*(2*m1 + m2)*np.sin(theta1) - m2*g*np.sin(theta1 - 2*theta2) - 2*np.sin(delta)*m2*(omega2**2*l2 + omega1**2*l1*np.cos(delta))) / (l1 * den)
    alpha2 = (2*np.sin(delta)*(omega1**2*l1*(m1 + m2) + g*(m1 + m2)*np.cos(theta1) + omega2**2*l2*m2*np.cos(delta))) / (l2 * den)
    
    return [omega1, alpha1, omega2, alpha2]

#solving the system of diffrential equations
S = solve_ivp(dotS, (0,10), S0, t_eval=ts)

#solutions for angles
theta1 = S.y[0,:]
theta2 = S.y[2,:]

#position of every mass
x1 = l1*np.sin(theta1)
y1 = -l1*np.cos(theta1)
x2 = x1+l2*np.sin(theta2)
y2 = y1-l2*np.cos(theta2)
th = S.t

#angle(time) dependency
plt.plot(ts,theta1, label='theta1')
plt.plot(ts,theta2, label='theta2')
plt.legend()
plt.xlabel('t')
plt.ylabel('theta1, theta2')
plt.show()
