#1) Use matplotlib to plot the following equation:
#y=x^2-x+2,add an annotation for the point (0,0)
import matplotlib.pyplot as plt
import math
import numpy as np
x=range(-10,10,1)
y=[n**2 -n +2 for n in x]
plt.plot(x,y)
plt.annotate('(0,0)', xy=(0, 0), xytext=(-3, 5),
             arrowprops={'facecolor': 'blue'})
plt.show()


#2) Create and label 4 seperate charts for the following
#equations (choose) a range for x that makes sense
#a)y=sqrt(x)
x=range(0,100,1)
y=[math.sqrt(n) for n in x]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('square root of x')
plt.show()
#b)y=x^3
x=range(-10,10,1)
y=[n**3 for n in x ]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('$x^3$')
#c)y=tan(x)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y=[np.tan(i)for i in x]
plt.plot(x,y)
plt.ylim(-5, 5)
plt.xlabel('$x$')
plt.ylabel('$tan(x)$')
plt.show()
#d)y=2^x
x=range(-10,10)
y=[2**n for n in x]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('$2^x$')
plt.show()
#You can use functions from the math module to help implement some of the equations above.
#3)Combine the figures you created in the last step into one large figure with 4 subplots.
plt.subplot(2,2,1)
x=range(0,100,1)
y=[math.sqrt(n) for n in x]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('square root of x')

plt.subplot(2,2,2)
x=range(-10,10,1)
y=[n**3 for n in x ]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('$x^3$')

plt.subplot(2,2,3)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y=[np.tan(i)for i in x]
plt.plot(x,y)
plt.ylim(-5, 5)
plt.xlabel('$x$')
plt.ylabel('$tan(x)$')

plt.subplot(2,2,4)
x=range(-10,10)
y=[2**n for n in x]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('$2^x$')
plt.show()

#4)Combine the figures you created in the last step into one figure where each of the 4 equations has a different color for the points.
#Be sure to include a legend.
x1=range(0,100,1)
y1=[math.sqrt(n) for n in x1]
plt.plot(x1,y1,c='yellow',label='$sqrt(x)$')
x2=range(-10,10,1)
y2=[n**3 for n in x2 ]
plt.plot(x2,y2,c='green',label='$x^3$')
x3 = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y3=[np.tan(i)for i in x3]
plt.plot(x3,y3,c='red',label='$tan(x)$')
x4=range(-10,10)
y4=[2**n for n in x4]
plt.plot(x4,y4,c='blue',label='$2^n$')
plt.legend(loc='upper right')
plt.ylim(-5,5)
plt.show()


