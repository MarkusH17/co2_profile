#returns diffusion coefficient in cm^2/s
#Chapman-Enskog Theory
import numpy as np

#parameters, from [1]
co2sig = 3.941 #angstrom
N2sig = 3.798 #angstrom
A = 1.859e-3 #atm*A^2*cm^2*g^0.5/(mol^0.5*s*K^1.5)
co2M = 44.01 #g/mol
N2M = 28 #g/mol
p = 1 #atm
sig = 0.5*(co2sig + N2sig) #angstrom
co2eps = 195.2 #K
N2eps = 71.4 #K
epsk = (N2eps*co2eps)**0.5 #K

#values determined from the appendix of:
# [1] D. T. Pratt and L. D. Smoot, Pulverized-coal combustion and gasification: Theory and applications for continuous flow processes. New York: Plenum Publishing Corporation, 1979. 

#collision integral estimated based on lennard-jones potential, Table B.4
#over the reasonable range of temperatures for a greenhouse the value of T* is about 2.5, a value of 1 is justifiable
omega = 1

def Deff(T):
    D = float(A*(T**1.5)*np.sqrt(1/co2M + 1/N2M) / (p * omega * sig**2))
    return D

