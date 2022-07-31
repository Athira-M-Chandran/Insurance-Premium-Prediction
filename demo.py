from Insurance.pipeline.pipeline import Pipeline
from Insurance.exception import ProjectException
from Insurance.logger import logging
from Insurance.config.configuration import Configuartion
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_validation_config = Configuartion().get_data_transformation_config()
        #print(data_validation_config)
       
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()