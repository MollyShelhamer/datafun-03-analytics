# ms_pythondataproject.py
# Python Data Project to retrieve files from a URL and process them

# Standard Python Library
import sys

# Local Logger module
from utils_logger import logger

# Local modules
from get_csv import main as get_csv_main
from get_json import main as get_json_main
from get_excel import main as get_excel_main
from get_text import main as get_text_main

from process_csv import process_csv_file
from process_json import process_json_file
from process_excel import process_excel_file
from process_text import process_text_file

# main function that takes file type as input
def main(file_type: str):
    if file_type == "csv":
        logger.info("Fetching and processing CSV data...")
        get_csv_main()         
        process_csv_file()     
    elif file_type == "json":
        logger.info("Fetching and processing JSON data...")
        get_json_main()
        process_json_file()
    elif file_type == "excel":
        logger.info("Fetching and processing Excel data...")
        get_excel_main()
        process_excel_file()
    elif file_type == "text":
        logger.info("Fetching and processing Text data...")
        get_text_main()
        process_text_file()
    else:
        logger.error(f"Unsupported file type: {file_type}")
        logger.error("Supported file types: csv, json, excel, text")
        sys.exit(1)


if __name__ == "__main__":
    main()
    
