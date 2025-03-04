import os
import sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.CaloryPrediction.exception import customException
from src.CaloryPrediction.logger import logging

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder


from src.CaloryPrediction.utils.utils import save_object



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def getDataTransformation(self):
        try :

            logging.info("Started getDataTransformation")
            gender_col = ['Gender']     # Gender will be one hot encoded
            numerical_cols = ['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']  # These columns will be scaled

            logging.info("Started Pipeline")

            logging.info("Started Gender Pipeline")
            gender_pipeline = Pipeline(steps=[
                ('encoder', OneHotEncoder())
            ])
            logging.info("Completed Gender Pipeline")

            logging.info("Started Numerical Pipeline")
            num_pipeline = Pipeline(steps=[
                ('scaler', StandardScaler())
            ])
            logging.info("Completed Numerical Pipeline")
            logging.info("Started Column Transformer")
            preprocessor=ColumnTransformer([
            ('gender_pipeline',gender_pipeline,gender_col),
            ('num_pipeline',num_pipeline,numerical_cols)
            ])
            logging.info("Completed getDataTransformation")
            
            return preprocessor


        except Exception as e :
            logging.info("Exception occured in getDataTransformation")
            raise customException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        logging.info("In initiate_data_transformation")
        try :

            logging.info("Started reading train and test data in initiate_data_transformation")

            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Completed reading train and test data in initiate_data_transformation")
            logging.info(f"Train Data Head : \n{train_df.head().to_string}")
            logging.info(f"Test Data Head : \n{test_df.head().to_string}")

            preprocessor_obj = self.getDataTransformation()

            target_column_name = 'Calories'
            drop_columns = [target_column_name,'User_ID']
            
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            return (
                train_arr,
                test_arr
            )

        except Exception as e :
            logging.info("Exception occured in initiate_data_transformation")
            raise customException(e,sys)

    