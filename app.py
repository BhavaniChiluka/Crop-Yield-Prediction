from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Home page

@app.route('/prediction')
def prediction_page():
    return render_template('predict.html')  # Prediction form page

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    year = request.form['Year']
    rainfall = request.form['average_rain_fall_mm_per_year']
    pesticides = request.form['pesticides_tonnes']
    temp = request.form['avg_temp']
    area = request.form['Area']
    item = request.form['Item']

    # Mock prediction logic
    prediction = f"Predicted yield for {item} in {area} (Year {year}): 2000 kg/hectare"

    return render_template('predict.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
