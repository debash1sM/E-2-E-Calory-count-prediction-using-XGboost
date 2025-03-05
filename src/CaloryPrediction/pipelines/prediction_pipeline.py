import os
import sys


from dataclasses import dataclass
from src.CaloryPrediction.logger import logging
from src.CaloryPrediction.exception import customException
from src.CaloryPrediction.utils.utils import load_object
import pandas as pd
import numpy as np

class Prediction:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            logging.info("Started Prediction Pipeline")
            pre_processor_path = os.path.join("artifacts","preprocessor.pkl")
            model_path = os.path.join("artifacts","model.pkl")

            pre_processor = load_object(pre_processor_path)
            model = load_object(model_path)


            scaled_data = pre_processor.transform(features)
            logging.info(f"features after scaled: {scaled_data}")
            prediction = model.predict(scaled_data)

            logging.info("Completed Prediction Pipeline")

            return prediction


        except customException as e:
            logging.error(e)


@dataclass
class CustomClass:
    Gender: str
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float

    def get_data_as_dataframe(self):
        try:
            data = {
                'Gender': [self.Gender],
                'Age': [self.Age],
                'Height': [self.Height],
                'Weight': [self.Weight],
                'Duration': [self.Duration],
                'Heart_Rate': [self.Heart_Rate],
                'Body_Temp': [self.Body_Temp]
            }
            df = pd.DataFrame(data)
            return df
        except Exception as e:
            raise customException(e, sys)


