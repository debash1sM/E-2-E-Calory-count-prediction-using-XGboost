from src.CaloryPrediction.pipelines.prediction_pipeline import Prediction, CustomClass
from src.CaloryPrediction.logger import logging
from src.CaloryPrediction.exception import customException
import os
import sys

if __name__ == "__main__":
    try:
        logging.info("Started Prediction")
        features = CustomClass("male",25,190.0,91.0,24.0,116.0,40.5)
        features_df = features.get_data_as_dataframe()
        logging.info(f"Features: {features_df.to_string(index=False)}")
        prediction_obj = Prediction()
        prediction = prediction_obj.predict(features_df)
        logging.info(f"Prediction: {prediction}")
        print(f"Prediction: {prediction} and original value is 180.0")
        logging.info("Completed Prediction")
        

        '''
            User_ID,Calories,Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp
            11932748,180.0,male,25,190.0,91.0,24.0,116.0,40.5
        '''
    except customException as e:
        logging.error(e)