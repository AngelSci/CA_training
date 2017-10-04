import numpy as np
from math import pi

def sphere_dist(P1, P2):
    """Computes surface distance between locations on Earth

    Assume spherical surface of Earth from (latitude,longitude) coordinates
    """
    R = 6365 # Radius of earth (km)
    lat1, long1 = P1 # extract lat/long coordinates
    x1 = np.cos(long1 * pi/180) * np.cos(lat1 * pi/180)
    y1 = np.sin(long1 * pi/180) * np.cos(lat1 * pi/180)
    z1 = np.cos(lat1 * pi/180) # trig functions are in radians
    R1 = np.array([x1,y1,z1]) # cartesian location of P1

    lat2, long2 = P2
    x2 = np.cos(long2 * pi/180) * np.cos(lat2 * pi/180)
    y2 = np.sin(long2 * pi/180) * np.cos(lat2 * pi/180)
    z2 = np.cos(lat2 * pi/180)
    R2 = np.array([x2,y2,z2]) # cartesian location of P2
    alpha = np.arccos(np.dot(R1,R2)) # angle in radians
    return R * alpha
