from flask import Flask, render_template, request
from ProductionCode.Goldilocks import Goldilocks_Determiner
from ProductionCode.load_data import take_exoplanet_data


app = Flask(__name__)
exoplanet_data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
goldilocks = Goldilocks_Determiner(exoplanet_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_goldilocks', methods=['POST'] )
def check_goldilocks():
    planet_name = request.form.get('planet_name')
    result = goldilocks.is_in_goldilocks_zone(planet_name)
    return render_template ('result.html', planet_name = planet_name, result = result)

if __name__ == "__main__":
    app.run(debug=True)