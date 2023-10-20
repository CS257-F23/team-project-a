#I used the following websites in doing this ID:
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

import ProductionCode.core as core
from flask import Flask, request, render_template

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
    #Gives info for how to navigate the app
    #Info written in the form of a html template  
    return render_template('homepage.html')

#Default route
@app.route('/about')
def about():
    """A route for an about page. Not yet implemented. No parameters.
    Param: none
    Returns: html page
    """
    #Gives info for how to navigate the app
    #Info written in the form of a html template  
    return render_template('about.html')

@app.route('/random_planet')
def random_planet():
    """A rotue that will be deleted later that currently leads to a 
     "feature not yet implemented" page that indicates the random planet
      feature is, believe it or not, not yet implemented. No parameters.
    Param: none
    Returns: html page
    """
    #Gives info for how to navigate the app
    #Info written in the form of a html template  
    return render_template('random_planet.html')

#Route with one parameter that shows planet info
@app.route('/planet_info''/<planet_name>', strict_slashes=False)
def get_cell(planet_name):
    """ 
    url route: Takes a planet name and creates a web page with that planet's info
    Param: string
    Returns: string
    """
    exoplanet_data = core.take_exoplanet_data()
    fixed_planet_name = underscores_to_spaces(planet_name)
    exoplanet_analyzer = core.exoplanetAnalyzer(exoplanet_data)
    exoplanet_info = exoplanet_analyzer.get_planet_info(fixed_planet_name)
    #This is needed for the render_template
    info_labels = exoplanet_analyzer.get_info_labels()
    return render_template ('planet_info.html', planet_name = fixed_planet_name, 
                            planet_info = exoplanet_info, info_labels = info_labels)


@app.route('/planet_info', methods = ['GET', 'POST'])
def planet_info():
    """ 
    POST route: Takes a planet name and creates a web page with that planet's info
    Param: string
    Returns: string
    """
    if request.method == 'POST': 
        planet_name = request.form['Search']
        exoplanet_data = core.take_exoplanet_data()
        fixed_planet_name = underscores_to_spaces(planet_name)
        exoplanet_analyzer = core.exoplanetAnalyzer(exoplanet_data)
        exoplanet_info = exoplanet_analyzer.get_planet_info(fixed_planet_name)
        #This is needed for the render_template
        info_labels = exoplanet_analyzer.get_info_labels()
        return render_template ('planet_info.html', planet_name = fixed_planet_name, 
                            planet_info = exoplanet_info, info_labels = info_labels)
    else:
        return "Not a valid request protocol"


if __name__ == '__main__':
    app.run()