
from scipy.integrate import odeint
from pylab import *

delta = .1
alfa = -.1
beta = .75

gamma = .5
omega = pi/2.

def dX_dt(X, t):
	return array([X[1], -delta*X[1] -alfa*X[0] - beta*X[0]**3 + gamma * cos(omega * t)])
	
t = linspace(0, 100, 1001)
X = odeint(dX_dt, [1., 0.], t)
x, v = X.T

f1 = figure('Dinamica')
plot(t, x, label='Posicion')
plot(t, v, label='Velocidad')
xlabel('Tiempo')
legend(loc='best')
grid()
show()

f2 = figure('Diagrama')
plot(x, v)
title('Diagrama de fases')
grid()
show()