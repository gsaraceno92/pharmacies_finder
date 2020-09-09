import sys,os
from typing import Any
from numbers import Real
import numpy as np


# The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes
def haversine_distance(base_latitude: Real, base_longitude: Real, latitude: Real, longitude: Real) -> float:
    r = 6371 # Earth radius
    phi1 = np.radians(base_latitude)
    phi2 = np.radians(latitude)
    delta_phi = np.radians(latitude - base_latitude)
    delta_lambda = np.radians(longitude - base_longitude)
    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)