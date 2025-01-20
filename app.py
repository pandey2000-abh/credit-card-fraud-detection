from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', prediction_text="")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input data from the form
        features = [float(request.form[f'v{i}']) for i in range(1, 29)]

        # Simulate a prediction (replace with your actual ML model logic)
        prediction = "Fraudulent" if sum(features) > 50 else "Non-Fraudulent"

        return render_template('index.html', prediction_text=f"Prediction: {prediction}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
