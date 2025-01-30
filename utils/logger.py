import logging
import os
from fileinput import filename
from pathlib import Path

class Logger:

    @staticmethod
    def get_logger(test_name="TestExecution",log_file="log.txt"):

        """
        Returns a logger instance that logs o a file in the outputs folder & the console
        :param log_file: Name of the log file
        :return: Logger instance
        """

        #Get the root directory of the project using Pathlib
        project_root = Path(__file__).resolve().parents[1]  #Get 1 levels from the current file
        # Define the log file path relative to the root directory (outputs folder)
        log_dir = os.path.join(project_root, "Logs")

        # Ensure the outputs directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # Create the folder if it doesn't exist

        # Full path to the log file
        log_file_path = os.path.join(log_dir, log_file)

        #Creating Logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)


        logging.basicConfig(filename=log_file_path,filemode='w',format=f'%(asctime)s - %(filename)s:[%(lineno)s] -%(levelname)s  - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(logging.DEBUG)



        return logger
