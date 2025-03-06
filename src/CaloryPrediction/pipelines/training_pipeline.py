from src.CaloryPrediction.components.data_ingestion import DataIngestion
from src.CaloryPrediction.components.data_transformation import DataTransformation
from src.CaloryPrediction.components.model_trainer import ModelTrainer

from src.CaloryPrediction.exception import customException
from src.CaloryPrediction.logger import logging


try:

    logging.info("Started Training Pipeline")
    logging.info("Started Data Ingestion")
    data_ingestion_obj = DataIngestion()
    train_data_path, test_data_path = data_ingestion_obj.initiateDataIngestion()   
    logging.info("Completed Data Ingestion")
    logging.info("Started Data Transformation")
    data_transformation_obj = DataTransformation()
    train_array,test_array = data_transformation_obj.initiate_data_transformation(train_data_path,test_data_path)
    logging.info(train_array[0])
    logging.info("Completed Data Transformation")
    logging.info("Started Model Training")
    model_trainer_obj = ModelTrainer()
    model_trainer_obj.initate_model_training(train_array,test_array)
    logging.info("Completed Model Training")
    logging.info("Completed Training Pipeline")
except customException as e:
    logging.error(e)





