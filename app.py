#We used the following websites in mking this:
#https://ttl255.com/jinja2-tutorial-part-2-loops-and-conditionals/#:~:text=For%20loops%20start%20with%20%7B%25,we%20go%20over%20the%20elements. 
#https://w3schools.com/cssref/pr_pos_right.php 
#https://www.w3schools.com/cssref/pr_background-image.php 
#https://www.w3schools.com/howto/howto_css_two_columns.asp 
#https://www.w3.org/MarkUp/HTMLPlus/htmlplus_45.html 
#https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML
#
#My photos come from the following websites:
#https://eos.org/articles/1-3-million-pairs-of-stars-surround-the-sun
#https://physicsworld.com/a/goldilocks-zone-may-not-be-a-good-metric-for-whether-life-exists-on-exoplanets-say-astrobiologists/ 
#https://nick-stevens.com/2017/05/27/exoplanet-rings-juno-based-textures/

from ProductionCode.Exoplanet_Data_Loader import data_loader
from ProductionCode.PlanetAnalyzer import exoplanetAnalyzer
from ProductionCode.Goldilocks import Goldilocks_Determiner
import random
from flask import Flask, request, render_template

exoplanet_data = data_loader("Data/ExoplanetSimplifiedData.csv")
exoplanet_analyzer = exoplanetAnalyzer(exoplanet_data.exoplanetsByName)
goldilocks_det = Goldilocks_Determiner(exoplanet_data.exoplanetsByName)
planet_list = list(exoplanet_data.exoplanetsByName.keys())
app = Flask(__name__)

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
    """A homepage route for the app. No parameters.
    Param: none
    Returns: html page
    """
    return render_template('homepage.html', planet_list= planet_list)

#Default route
@app.route('/about')
def about():
    """A route for an about page. Not yet implemented. No parameters.
    Param: none
    Returns: html page
    """
    #Gives info for how to navigate the app
    #Info written in the form of a html template  
    return render_template('about.html', planet_list= planet_list)

@app.route('/learn')
def learn():
    """A route for a learn page.
    Param: none
    Returns: html page
    """
    #Gives info about the meaning of goldilocks zone
    #Info written in the form of a html template  
    return render_template('learn.html', planet_list= planet_list)

@app.route('/available_planets')
def available_planets():
    """A route for a page which shows all planet options.
    Param: none
    Returns: html page
    """
    #Gives info about the meaning of goldilocks zone
    #Info written in the form of a html template  
    return render_template('available_planets.html', planet_list= planet_list)

@app.route('/habitable_planets')
def habitable_planets():
    """A route for a page which shows all habitable planets.
    Param: none
    Returns: html page
    """
    #Gives info about the meaning of goldilocks zone
    #Info written in the form of a html template  
    return render_template('habitable_planets.html', planet_list= planet_list)


@app.route('/random_planet')
def random_planet():
    """A rotue that will be deleted later that currently leads to a 
     "feature not yet implemented" page that indicates the random planet
      feature is, believe it or not, not yet implemented. No parameters.
    Param: none
    Returns: html page
    """
    random_num = random.randint(0, 5523)
    planet_name = planet_list[random_num]
    exoplanet_info = exoplanet_analyzer.get_formatted_planet_info_list(planet_name)
    goldilocks_result = goldilocks_det.get_goldilocks_zone(planet_name)
    return render_template ('planet_info.html', planet_name = planet_name, 
                            planet_info = exoplanet_info, planet_list= planet_list, goldilocks_result= goldilocks_result)

#Route with one parameter that shows planet info
@app.route('/planet_info''/<planet_name>', strict_slashes=False)
def get_planet_info(planet_name):
    """ 
    url route: Takes a planet name and creates a web page with that planet's info
    Param: string
    Returns: string
    """
    fixed_planet_name = underscores_to_spaces(planet_name)
    exoplanet_info = exoplanet_analyzer.get_formatted_planet_info_list(fixed_planet_name)
    goldilocks_result = goldilocks_det.is_in_goldilocks_zone(planet_name)
    return render_template ('planet_info.html', planet_name = fixed_planet_name, 
                            planet_info = exoplanet_info, planet_list= planet_list, goldilocks_result = goldilocks_result)


@app.route('/planet_info', methods = ['GET', 'POST'])
def planet_info():
    """ 
    POST route: Takes a planet name and creates a web page with that planet's info
    Param: string
    Returns: string
    """
    if request.method == 'POST': 
        planet_name = request.form['planet_name']
        exoplanet_info = exoplanet_analyzer.get_formatted_planet_info_list(planet_name)
        goldilocks_result = goldilocks_det.get_goldilocks_zone(planet_name)
        return render_template ('planet_info.html', planet_name = planet_name, 
                            planet_info = exoplanet_info, planet_list= planet_list, goldilocks_result= goldilocks_result)
    else:
        return "Not a valid request protocol"


if __name__ == "__main__":
    app.run(debug=True)