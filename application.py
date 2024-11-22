from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the Ridge model and StandardScaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))


@app.route("/")
def index():
    return render_template('index.html')  # Render the main page


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        try:
            # Retrieve data from the form
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            # Preprocess and predict
            new_data_scaled = standard_scaler.transform(
                [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
            )
            result = ridge_model.predict(new_data_scaled)

            # Render the result
            return render_template('home.html', results=result[0])
        except Exception as e:
            return render_template('home.html', results=f"Error: {str(e)}")
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
