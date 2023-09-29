from math import sqrt
from exoplanet_data_reader import exoplanetDictionary

def get_stellar_lum(planet_name):
    """ Function that takes planet name and returns it's stellar luminosity"""
    planet_info = exoplanetDictionary[planet_name]
    stellar_lum = planet_info[13]
    
    return stellar_lum

def get_sm_axis(planet_name):
    """ Function that takes planet name and returns it's semi-major axis"""
    planet_info = exoplanetDictionary[planet_name]
    sm_axis = planet_info[8]
    
    return sm_axis

def determine_goldilocks_zone(planet_name):
    """ Function that takes planet name and uses returns an ordered pair (inner, outer) bound"""
    stellar_lum = get_stellar_lum(planet_name)
    inner_bound = sqrt(stellar_lum / 1.1)
    outer_bound = sqrt(stellar_lum / 0.53)

    return (inner_bound, outer_bound)

def is_in_goldilocks_zone(planet_name):
    """ Takes planet name and returns boolean yes or no corresponding 
        with if the planet is within the bounds of it's goldilocks zone 
    """
    planet_stellar_dist = get_sm_axis(planet_name)
    goldilocks_zone = determine_goldilocks_zone
    if goldilocks_zone[0] < planet_stellar_dist < goldilocks_zone[1]:
        return True
    else:
        return False
