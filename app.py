from flask import Flask, request, render_template
from src.CaloryPrediction.pipelines.prediction_pipeline import Prediction, CustomClass
from src.CaloryPrediction.logger import logging
from src.CaloryPrediction.exception import customException
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        Gender = request.form['Gender']
        Age = int(request.form['Age'])
        Height = float(request.form['Height'])
        Weight = float(request.form['Weight'])
        Duration = float(request.form['Duration'])
        Heart_Rate = float(request.form['Heart_Rate'])
        Body_Temp = float(request.form['Body_Temp'])

        # Create an instance of CustomClass with input data
        input_data = CustomClass(
            Gender=Gender,
            Age=Age,
            Height=Height,
            Weight=Weight,
            Duration=Duration,
            Heart_Rate=Heart_Rate,
            Body_Temp=Body_Temp
        )

        # Get the data as a DataFrame
        input_df = input_data.get_data_as_dataframe()

        # Log the input data
        logging.info(f"Input Data:\n{input_df.to_string(index=False)}")

        # Create an instance of Prediction and make a prediction
        prediction_pipeline = Prediction()
        prediction = prediction_pipeline.predict(input_df)

        # Log the prediction
        logging.info(f"Prediction: {prediction} :: type = {type(prediction[0])}")

        formatted_prediction = f'{prediction[0]:.2f}'

        return render_template('result.html', prediction=formatted_prediction)

    except customException as e:
        logging.error(e)
        return render_template('index.html', prediction_text='An error occurred during prediction.')

if __name__ == "__main__":
    app.run(debug=True)