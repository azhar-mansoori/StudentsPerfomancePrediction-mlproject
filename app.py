from src.mlproject.logger import logging 
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion,DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_tranier import ModelTrainer,ModelTrainerConfig






if __name__== "__main__":
    logging.info("the execution has strated")



    try:
         data_ingestion = DataIngestion()
         train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()



         data_transformation = DataTransformation()
         train_array,test_array,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)


         model_trainer  = ModelTrainer()
         print(model_trainer.initiate_model_trainer(train_array,test_array))



        
    except Exception as e :
         logging.info("custom exception")
         raise CustomException(e,sys)    