import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pymysql

import pickle
import numpy as np

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')
charset=os.getenv('charset')



def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            charset=charset
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print("1")
        print(df)
        print("2")
        print(df.head())
        return df



    except Exception as ex:
        raise CustomException(ex)
    



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    
    
    
#function for model evaluation with results --> models : r2 score
def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        report={}
        for i in range (len(list(models))):
            model = list(models.values())[i]
            para=params[list(models.keys())[i]]


            #apply grid search cv
            gs=GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            #model training 
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #predictions
            y_train_pred = model.predict(X_train)
            Y_test_pred = model.predict(X_test)

            #r2 score
            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,Y_test_pred)

            report[list(models.keys())[i]]=test_model_score

            return report
        
    except Exception as e:
        raise CustomException(e,sys)
    


#function to load the pickle file
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    


