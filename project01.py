import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
# from numpy import as nm

'g1(y,t) function'
k = 30
g = 9.81;
l = .8
m_0 = 0.5;
b = 0.02
c = 0
r = 0.0
h = 1;
# m = lambda t: m_0 - r*t

def g1(y1, y2, t):
    return y2


'g2(y,t) function'


def g2(y1, y2, t):

    return (h*h*math.cos(y1)/(math.sin(y1))**3)-((g/l)*math.sin(y1))-b*y2;
    # return ((r*y2+(h*h*math.cos(y1))/(m_0 - r*t)(math.sin(y1))**3)-(m_0 - r*t)*(g/l)*math.sin(y1))/(m_0 - r*t)


def g3(z1, z2, y1, y2, t):
    return z2

'g2(y,t) function'


def g4(y1, y2, t):

    return h / (math.sin(y1)) ** 2
    # return h/((m_0 - r*t)*(math.sin(y1))**2)


'Calculating c1-4 coefficient for RK'


def coef(g, y1, y2,  t, tau):
    c1 = tau * g(y1, y2, t)
    c2 = tau * g(y1 + c1 / 2, y2 + c1 / 2, t + tau / 2)
    c3 = tau * g(y1 + c2 / 2, y2 + c2 / 2,  t + tau / 2)
    c4 = tau * g(y1 + c3, y2 + c3,  t + tau)

    return (c1 + 2 * c2 + 2 * c3 + c4) / 6


'Initialization'
t = 0  # Initial time
y1 = [math.pi/12]  # at t = 0, y(0) = 0
y2 = [math.pi/2]  # at t = 0, y'(0) = 1
z1 = [0];

time = [0]
tau = 0.01  # Step size

x1 = [];
x2 = [];
x3 = [];
e = [0]

while t < 100:
    'y(i+1) = y(i) + coef(y(i), t, tau)'
    # if (z2[-1] + coef(g4, z1[-1], z2[-1], y1[-1], y2[-1], t, tau))<=math.sqrt(g/l):
    y1.append(y1[-1] + coef(g1, y1[-1], y2[-1],  t, tau))
    y2.append(y2[-1] + coef(g2, y1[-1], y2[-1],  t, tau))
    z1.append(z1[-1]+ coef(g4,  y1[-1], y2[-1],  t, tau));
    x1.append(l * math.sin(y1[-1]) * math.cos(z1[-1]));
    x2.append(l * math.sin(y1[-1]) * math.sin(z1[-1]));
    x3.append(-(l * math.cos(y1[-1])))
    # e.append(- m*g*l * math.cos(y1[-1]))
    time.append(t)

    t += tau


fig = plt.figure();
ax = plt.gca(projection="3d");
plt.plot(x1, x2,x3, label = 'e');
plt.title("Initial condition: y1="+str(y1[0])+" y2="+str(y2[0])+" z1="+str(z1[0])+" h="+str(h));
# plt.plot(time, z2, label = 'z2')
# plt.plot(time, z1 ,label = 'y2')
# plt.plot(x1, x2, x3, label = 'points')
# plt.plot(time, y1, label = 'time vs theta')
# plt.plot(time, z1, label = 'time vs phi')
# plt.plot(time, y2, label = 't vs v_theta')
# plt.plot(time, z2)
# plt.figure(1)
# plt.plot(y1, y2, label = 'theta vs v_theta')
# plt.xlabel('Time in sec.')
# plt.ylabel('Magnitude')
# plt.legend(['y1', 'y2'])

# plt.figure(2)
# plt.plot(x1, x2);
# plt.plot(time, y2)
# plt.plot(time, y1, label = 'tangential velocity')
# plt.plot(time, z2, label = 'angular velocity')

# plt.xlabel('y1')
# plt.ylabel('y2')
# plt.legend()
plt.legend()
# print(y1)

plt.show()
