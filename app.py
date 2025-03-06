from flask import Flask, request, render_template
from src.CaloryPrediction.pipelines.prediction_pipeline import Prediction, CustomClass
from src.CaloryPrediction.logger import logging
from src.CaloryPrediction.exception import customException
import mysql.connector
import numpy as np
import os

# # Database configuration
# db_config = {
#     'user': os.getenv('MYSQL_USER', 'root'),
#     'password': os.getenv('MYSQL_PASSWORD', 'mysql'),
#     'host': os.getenv('MYSQL_HOST', 'db'),
#     'database': os.getenv('MYSQL_DB', 'calory_prediction')
# }
# db_config = {
#     'user': 'root',
#     'password': 'mysql',
#     'host': 'localhost',
#     'database': 'calory_prediction'
# }

app = Flask(__name__)

# def init_db():
#     try:
#         # conn = mysql.connector.connect(**db_config)
#         # cursor = conn.cursor()
#         # # Check if the table exists
#         # cursor.execute("""
#         # SELECT COUNT(*)
#         # FROM information_schema.tables
#         # WHERE table_name = 'predictions'
#         # """)
#         # if cursor.fetchone()[0] == 0:
#         #     # Create the table if it does not exist
#         #     create_table_query = """
#         #     CREATE TABLE predictions (
#         #         id INT AUTO_INCREMENT PRIMARY KEY,
#         #         gender VARCHAR(10),
#         #         age INT,
#         #         height FLOAT,
#         #         weight FLOAT,
#         #         duration FLOAT,
#         #         heart_rate FLOAT,
#         #         body_temp FLOAT,
#         #         prediction FLOAT,
#         #         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         #     );
#         #     """
#         #     cursor.execute(create_table_query)
#         #     conn.commit()
#         #     print("Table 'predictions' created in MySQL database.")
#         # else:
#         #     print("Table 'predictions' already exists in MySQL database.")
#         # cursor.close()
#         # conn.close()
#         print("Database did not initialized.")
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")

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

        # Convert numpy.float32 to native Python float
        prediction_value = float(prediction[0])

        formatted_prediction = f'{prediction_value:.2f}'

        try:
            # Insert data into MySQL database
            # conn = mysql.connector.connect(**db_config)
            # cursor = conn.cursor()
            # insert_query = """
            # INSERT INTO predictions (gender, age, height, weight, duration, heart_rate, body_temp, prediction)
            # VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            # """
            # cursor.execute(insert_query, (Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp, prediction_value))
            # conn.commit()
            # cursor.close()
            # conn.close()
            print("Data inserted into MySQL database.")
        except customException as e:
            logging.error(e)
        finally:
            return render_template('result.html', prediction=formatted_prediction)

    except customException as e:
        logging.error(e)
        return render_template('index.html', prediction_text='An error occurred during prediction.')

if __name__ == "__main__":
    #init_db()
    app.run(debug=True, host='0.0.0.0')