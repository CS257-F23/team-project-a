from flask import Flask, render_template
from ProductionCode.Goldilocks import Goldilocks_Determiner
from ProductionCode.Exoplanet_Data_Loader import data_loader
from ProductionCode.PlanetAnalyzer import *


app = Flask(__name__)
exoplanet_data = data_loader('Data/ExoplanetSimplifiedData.csv')

def underscores_to_spaces(underscored_string):
    """ 
    Takes a string and converts all underscores in it to spaces
    Param: string
    Returns: string
    """
    better_string =''
    for character in underscored_string:
        if character == '_':
            better_string = better_string + " "
        else:
            better_string = better_string + character
    return better_string

#Default route
@app.route('/')
def homepage():
    """A homepage route for the app. No parameters."""
    #Gives info for how to navigate the app
    #Info written in the form of a html template  
    return render_template('homepage.html')

#Route with one parameter that shows planet info
@app.route('/check_goldilocks''/<planet_name>', strict_slashes=False)
def check_goldilocks(planet_name):
    """ 
    Takes a planet name and creates a web page that shows if that planet is in the Goldilocks Zone
    Param: string
    Returns: string
    """
    fixed_planet_name = underscores_to_spaces(planet_name)
    goldilocks_analyzer = Goldilocks_Determiner(exoplanet_data.exoplanetsByName)
    result = goldilocks_analyzer.is_in_goldilocks_zone(fixed_planet_name)

    #Change the html input based on if the planet is in the Goldilocks Zone
    if result == True:
        return render_template ('goldilocks_result.html', planet_name = planet_name,  
                                result = "is in the Goldilocks Zone! (by Solar Equivalent AU)")
    elif result == None:
        return render_template ('goldilocks_result.html', planet_name = planet_name,  
                                result = "could be in the Goldilocks Zone, but unfortunately our database does not contain enough information to tell.")
    else:
        return render_template ('goldilocks_result.html', planet_name = planet_name, 
                                result = "is not in the Goldilocks Zone. (by Solar Equivalent AU)")

#Route with one parameter that shows planet info
@app.route('/planet_info''/<planet_name>', strict_slashes=False)
def get_planet_info(planet_name):
    """ 
    Takes a planet name and creates a web page with that planet's info
    Param: string
    Returns: string
    """
    fixed_planet_name = underscores_to_spaces(planet_name)
    exoplanet_analyzer = exoplanetAnalyzer(exoplanet_data.exoplanetsByName)
    exoplanet_info = exoplanet_analyzer.get_html_formatted_planet_info(fixed_planet_name)
    return exoplanet_info

#Route for errors
@app.errorhandler(404)
def page_not_found(e):
    """Returns a 404 message"""
    return render_template ('404.html')

#Route for errors
@app.errorhandler(500)
def page_not_found(e):
    """Returns an error message"""
    return render_template ('500.html')

if __name__ == "__main__":
    app.run(debug=True)