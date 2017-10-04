import numpy as np
from math import pi

def spherical_to_cartesian(lat, lon):
    if np.fabs(lat) > 90:
        raise ValueError('Invalid latitude %s' % lat)
    if np.fabs(lon) > 180:
        raise ValueError('Invalid longitude %s' % lon)

    lat, lon = deg_to_rad(lat), deg_to_rad(lon)
    x1 = np.cos(lon) * np.cos(lat)
    y1 = np.sin(lon) * np.cos(lat)
    z1 = np.cos(lat) # trig functions are in radians
    return np.array([x1,y1,z1]) # cartesian location of P1

def deg_to_rad(a):
    if not(np.all(np.isfinite(a))):
        raise ValueError('Non-finite values in deg_to_rad')
    return a * pi / 180

def sphere_dist(P1, P2):
    """Computes surface distance between locations on Earth

    Assume spherical surface of Earth from (latitude,longitude) coordinates
    """
    R = 6365 # Radius of earth (km)
    R1 = spherical_to_cartesian(*P1)
    R2 = spherical_to_cartesian(*P2)

    alpha = np.arccos(np.dot(R1,R2)) # angle in radians
    return R * alpha
