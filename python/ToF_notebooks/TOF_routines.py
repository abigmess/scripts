import numpy as np

h=6.62607004e-34 #Planck constant [m^2 kg / s]
m=1.674927471e-27 #Neutron mass [kg]

def tof2l(tof, lambda0, t0, L):
    l=lambda0+h/m*(tof-t0)/(L)/1e-10
    return l

def l2tof(l, lambda0, to0, L):
    tof=t0+(l*1e-10)*(L)*m/h
    return tof

def binning (mysignal, newsize):
    binned_signal = np.zeros(newsize)
    bin_size = int(len(mysignal)/newsize)
    for i in range(0, newsize):
        bin_value = np.median(mysignal[i*bin_size:i*bin_size+bin_size])
        binned_signal[i]=bin_value
    
    return (binned_signal)

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return (idx)
