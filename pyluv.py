#!/usr/bin/env python  
import matplotlib  
import numpy as np  
import matplotlib.cm as cm  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
import sys  
from matplotlib.colors import LinearSegmentedColormap  
  
matplotlib.rcParams['xtick.direction'] = 'out'  
matplotlib.rcParams['ytick.direction'] = 'out'  
  
def r(x, x0, y, y0):  
  return np.sqrt((x-x0)*(x-x0) + (y-y0)*(y-y0))  
  
def createSoundPlot(wavelength, phasediff_deg, x1, y1, x2, y2):  
    phasediff = phasediff_deg * np.pi / 180  
  
    delta = 0.025  
    x = np.arange(-1, 5, delta)  
    y = np.arange(-3, 3, delta)  
    X, Y = np.meshgrid(x, y)  
  
    Z1 = np.sin((r(X, x1, Y, y1)/wavelength) * 2 * np.pi) # sound wave 1  
    Z2 = np.sin((r(X, x2, Y, y2)/wavelength) * 2 * np.pi + phasediff) # sound wave 2  
    Z = Z1 + Z2  
  
    extent = (-1,5,-3,3)  
    im = plt.imshow(Z, interpolation='nearest', extent=extent, vmin=0, vmax=1, cmap=plt.cm.gray_r) # Plot waves in inverted grayscale  
    plt.colorbar(im)  
    plt.show()  
  
createSoundPlot(3.4, 5.2, 1.0, 0.0, 1.1, 0.0)  