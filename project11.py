#importing all necessary library
import matplotlib.pyplot as plt;
import math;
from mpl_toolkits.mplot3d import Axes3D;


#here I use the constant
g= 9.812;
l = 1;
h = 1;
m = .5;
u = 0;


#
def g1(y1, y2, z1, z2,  t):
    return y2;

# here impliment the math of the form
# y2'' = -(g/l)sin(y1) + h^2(cos(y1)/(sin(y1)^3)
def g2(y1, y2, z1, z2, t):
    return (-g*m*math.sin(y1)+l*m*math.sin(y1)*math.cos(y1)*z2**2-l*u*y2)/(l*m);

def g3(y1, y2, z1, z2, t):
    return z2;

def g4(y1, y2, z1, z2, t):
    return (-2*l*m*y2*math.sin(y1)*math.cos(y1)*z2 - l*u*(math.sin(y1))**2*z2)/(l*m*(math.sin(y2))**2);


# fig ----> is the function name
# y1 -----> is the main function
# y2 -----> is the derivative of the function
# t ------> is the time
# tau ----> is the time interval

def coefficient(fig, y1, y2, z1, z2, t, tau):
    k1 = tau*fig(y1, y2,z1, z2, t);
    k2 = tau*fig(y1+k1/2, y2+k1/2,z1+k1/2, z2+k1/2, t+tau/2);
    k3 = tau*fig(y1+k2/2, y2+k2/2, z1+k2/2, z2+k2/2, t+tau/2);
    k4 = tau*fig(y1+k3, y2+k3,z1+k3,z2+k3, t+tau);

    return (k1+ 2*k2+ 2*k3+ k4)/6;


# Rangu-kutta method
def RanguKutta():
#     here the initial value are set
    tau = 0.01; # time interval
    t =0; # starting time
    y1 = [math.pi/12];
    y2 = [math.pi/2];
    z1 = [0];
    z2 = [.3];
    time = [t]; # recording time

    x1 = [];
    x2 = [];
    x3 = [];

    while t<10:
        y1.append(y1[-1] + coefficient(g1, y1[-1], y2[-1],z1[-1], z2[-1], t, tau));
        y2.append(y2[-1] + coefficient(g2, y1[-1], y2[-1], z1[-1], z2[-1], t, tau));
        z1.append(z1[-1] + coefficient(g3, y1[-1], y2[-1], z1[-1], z2[-1], t, tau));
        # z2.append(z2[-1] + coefficient(g4, y1[-1], y2[-1], z1[-1], z2[-1], t, tau));

        # position
        x1.append(l * math.sin(y1[-1]) * math.cos(z1[-1]));
        x2.append(l * math.sin(y1[-1]) * math.sin(z1[-1]));
        x3.append(-(l * math.cos(y1[-1])))

        t = t+tau;
        time.append(t);

    return [[time, y1, y2, z1, z2],[x1, x2, x3]];



r = RanguKutta();


# 3D
# fig = plt.figure();
# ax = plt.gca(projection="3d");
# plt.plot(r[1], r[2], r[0], label="e");

fig = plt.figure();
ax = plt.gca(projection='3d');
plt.plot(r[1][0], r[1][1], r[1][2], label = 'e');

# plt.plot(r[0][4], r[0][1], label = 'e');

# plt.xlabel("time");
# plt.ylabel("z2");
plt.title("Initial condition: y1="+str(r[0][1][0])+" y2="+str(r[0][2][0])+" z1="+str(r[0][3][0]));

plt.show();
