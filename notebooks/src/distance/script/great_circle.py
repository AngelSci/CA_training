#!/usr/bin/env python

import numpy as np
from math import pi

lat1, long1 = (51.5, -0.1) # london
lat2, long2 = (40.7, -74.0) # new york

x1 = np.cos(long1 * pi/180) * np.cos(lat1 * pi/180)
y1 = np.sin(long1 * pi/180) * np.cos(lat1 * pi/180)
z1 = np.cos(lat1 * pi/180) # trig functions are in radians
R1 = np.array([x1,y1,z1]) # cartesian location of P1

x2 = np.cos(long2 * pi/180) * np.cos(lat2 * pi/180)
y2 = np.sin(long2 * pi/180) * np.cos(lat2 * pi/180)
z2 = np.cos(lat2 * pi/180)
R2 = np.array([x2,y2,z2]) # cartesian location of P2
alpha = np.arccos(np.dot(R1,R2)) # angle in radians

R = 6365
dist = R * alpha

print(dist)
