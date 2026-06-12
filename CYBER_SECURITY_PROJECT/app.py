from flask import Flask, render_template, request
import numpy as np
from joblib import load

app = Flask(__name__)

model = load("random_forest_model_4_features.joblib")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        feature_values = []

        html_input_names = [
            "flow_duration",
            "total_fwd_packets",
            "total_backward_packets",
            "total_length_fwd_packets"
        ]

        for name in html_input_names:
            feature_values.append(float(request.form[name]))

        input_data = np.array([feature_values])

        prediction = model.predict(input_data)[0]

        return render_template(
            "index.html",
            prediction=prediction
        )

    except Exception as e:
        return f"Prediction Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
