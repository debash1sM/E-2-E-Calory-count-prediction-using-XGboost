import os
import pandas as pd
import sys
from src.CaloryPrediction.logger import logging
from src.CaloryPrediction.exception import customException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


class DataIngestionConfig:
    raw_data_path : str = os.path.join("artifacts","raw.csv")
    train_data_path : str = os.path.join("artifacts","train.csv")
    test_data_path : str = os.path.join("artifacts","test.csv")



class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiateDataIngestion(self):
        logging.info("Data Ingestion Started")

        try:
            calories = pd.read_csv(os.path.join("notebooks/data","calories.csv"))
            exercise = pd.read_csv(os.path.join("notebooks/data","exercise.csv"))
            logging.info("Successfully read the data in df")

            logging.info("Merging the dataframes")
            df = pd.merge(calories,exercise,on="User_ID")

            logging.info(df.shape)
            


            logging.info("Starting to save raw_data in artifacts")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Successfully saved raw_data in artifacts")



            logging.info("Performing train test split")
            train_data,test_data = train_test_split(df,test_size=0.25)
            logging.info("Data has been splitted into train and test")


            logging.info("Starting to save train_data in artifacts")
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            logging.info("Successfully saved train_data in artifacts")


            logging.info("Starting to save test_data in artifacts")
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("Successfully saved test_data in artifacts")

            logging.info("Data Ingestion success")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e :
            logging.info("Exception occured in Data Ingestion")
            raise customException(e,sys)

    