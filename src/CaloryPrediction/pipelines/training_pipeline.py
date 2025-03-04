from src.CaloryPrediction.components.data_ingestion import DataIngestion
from src.CaloryPrediction.components.data_transformation import DataTransformation
from src.CaloryPrediction.components.model_trainer import ModelTrainer

from src.CaloryPrediction.exception import customException
from src.CaloryPrediction.logger import logging


obj = DataIngestion()
train_data_path, test_data_path = obj.initiateDataIngestion()   
print(train_data_path, test_data_path)



