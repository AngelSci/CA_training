from math import pi
import numpy as np

def spherical_to_cartesian(P):
    """Returns the cartesian location for a given position in latidude and longitude

    returns a numpy array of x,y,z coordinates
    """
    lat, lon = P

    lat_rad = deg_to_rad(lat)
    lon_rad = deg_to_rad(lon)

    x1 = np.cos(lon_rad) * np.cos(lat_rad)
    y1 = np.sin(lon_rad) * np.cos(lat_rad)
    z1 = np.cos(lat_rad)
    return np.array([x1,y1,z1])


def deg_to_rad(a):
    """Converts degrees to radians"""
    return a * pi/180


def sphere_dist2(P1, P2):
    """Computes surface distance between locations on Earth

    Assume spherical surface of Earth from (latitude,longitude) coordinates
    """
    R1 = spherical_to_cartesian(P1)
    R2 = spherical_to_cartesian(P2)

    R = 6365
    alpha = np.arccos(np.dot(R1,R2))
    return R * alpha
