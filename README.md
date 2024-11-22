
# Forest Fire Prediction Web Application 🌳🔥

This repository contains a **Flask-based web application** that predicts forest fire risks based on various meteorological and environmental parameters using a **Ridge Regression Model**.

---

## Features

- **User-friendly Interface**: Input relevant parameters via a web form.
- **Machine Learning Model**: Utilizes a trained Ridge Regression model for predictions.
- **Scalable Design**: Includes a pre-trained **StandardScaler** for input data preprocessing.
- **Real-time Prediction**: Get immediate insights into forest fire risks.

---
## Installation and Setup

### Create a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Prepare Models:

Ensure the following files are present in the `models/` directory:
- `ridge.pkl` (pre-trained Ridge Regression model)
- `scaler.pkl` (fitted StandardScaler)

### Run the Application:

```bash
python application.py
```

### Access the Application:

Open your browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Usage

1. Navigate to the **home page**.
2. Fill in the required parameters:
   - **Temperature**: Ambient temperature in degrees Celsius.
   - **RH**: Relative humidity percentage.
   - **Ws**: Wind speed.
   - **Rain**: Rainfall in mm.
   - **FFMC**: Fine Fuel Moisture Code.
   - **DMC**: Duff Moisture Code.
   - **ISI**: Initial Spread Index.
   - **Classes**: Forest type class as numeric input.
   - **Region**: Region code.
3. Click **Predict** to see the forecasted forest fire risk.

---

## Project Structure

```plaintext
.
├── application.py        # Main Flask application
├── templates/            # HTML templates for rendering
│   ├── index.html
│   └── home.html
├── models/               # Pre-trained models
│   ├── ridge.pkl
│   └── scaler.pkl
├── static/               # Static files (CSS, JS, images)
└── requirements.txt      # Required Python packages
```

---

## Future Improvements

- Extend support for additional meteorological parameters.
- Integrate more sophisticated machine learning models.
- Add visualization for prediction results.
- Deploy the application on cloud platforms like AWS or Heroku.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

---

## Author

**Ashes Kumar Nanda**  
Feel free to connect on [LinkedIn](www.linkedin.com/in/ashes-nanda-59bb35251) or [GitHub](https://github.com/Ashes-Nanda).
