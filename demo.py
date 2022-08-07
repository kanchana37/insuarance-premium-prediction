from insurance.pipeline.pipeline import Pipeline
from insurance.exception import PackageException
from insurance.logger import logging
from insurance.config.configuration import Configuration
import sys
import os

def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        pipeline.start()
        logging.info("main function execution completed.")

    except Exception as e:
        raise PackageException(e, sys) from e
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()