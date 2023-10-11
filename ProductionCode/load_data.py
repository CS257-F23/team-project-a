import csv

def take_exoplanet_data(exoplanetData) :
    """
    Takes a csv file of exoplanet data and returns a 
    dictionary of planets keyed to lists containing 
    all the info about them. 
    Param: string
    Returns: dictionary
    """
    #Make an empty dictionary
    exoplanetsByName = {}

    with open(exoplanetData, 'r') as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            exoplanetsByName = add_row_of_data_to_dictionary(row, exoplanetsByName)

        return exoplanetsByName

def add_row_of_data_to_dictionary(row, exoplanetsByName):
    """
    Helper function for take_exoplanet_data. 
    Adds one planet's worth of info into a growing dictionary of info by planet.
    Param: dictionary, dictionary 
    Returns: dictionary
    """
    
    #Save all the important data from each planet
    planetName = row['pl_name']
    hostName = row['hostname']
    numberOfStars = row['sy_snum']
    numberOfPlanets = row['sy_pnum']
    numberOfMoons = row['sy_mnum']
    discoveryMethod = row['discoverymethod']
    discoveryYear = row['disc_year']
    discoveryFacility = row['disc_facility']
    semiMajorAxis = row ['pl_orbsmax']
    planetRadius = row['pl_rade']
    planetMass = row['pl_bmasse']
    stellarRadius = row ['st_rad']
    stellarMass = row['st_mass']
    stellarLuminosity = row ['st_lum']
    galacticLatitude = row ['glat']
    galacticLongitude = row ['glon']

    #Make that planet an entry in the dictionary
    if planetName not in exoplanetsByName :
        #Put the data in a list 
        exoplanetsByName[planetName] = [planetName, hostName, numberOfStars, numberOfPlanets,
                                        numberOfMoons, discoveryMethod, discoveryYear, discoveryFacility, 
                                        semiMajorAxis, planetRadius, planetMass, stellarRadius, stellarMass, 
                                        stellarLuminosity, galacticLatitude, galacticLongitude]
    return exoplanetsByName
                
