import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import csv
import json
import pandas as pd
import logging
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# POSTGRES SERVER DETAILS
table_name = "universities"
postgres_user = os.getenv("DB_username")
postgres_password = os.getenv("DB_password")
postgres_host = os.getenv("DB_host")
postgres_port = os.getenv("DB_port")
postgres_DB = os.getenv("DB_name")

# MYSQL SERVER DETAILS
mysql_host = os.getenv("host")
mysql_port = os.getenv("port")
mysql_user = os.getenv("user")
mysql_password = os.getenv("password")
mysql_DB = os.getenv("database")


# Set up logging
log_filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Also set up logging to print to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(console_handler)

# Log the start of the script
logging.info("Script started.")

site = "https://en.wikipedia.org/wiki/List_of_largest_universities"
csv_file = "universities-data.csv"
json_file = "universities-data.json"
action = "w"

def get_data():
    # this function downloads the html data of the wikipedia site:
    html_page = requests.get(site)
    soup = BeautifulSoup(html_page.content,"html.parser")
    table = soup.find("table",class_="sortable wikitable")
    trs = table.find_all("tr") # trs stand for table rows
    
    return trs

def extract_column_header():
    # the function extract the column header for the table
    column_header = list(map(lambda x: x.text.strip(), get_data()[0].find_all("th")))
    column_header[-1] = "Link"
    return column_header
# the map function applies a function on every element in a given list
# in the above code (lambda x: x.text.strip()) is the function that will be applied on every limit of the list

def extract_single_row(tr):
    # the function extracts a single row
    row_soup = tr.findAll("td")
    row = list(map(lambda x: x.text.strip(),row_soup))
    if len(row) < 6:
        row.append("")
    link = row_soup[1].a.attrs["href"].lstrip("/")
    row[-1] = f"https://en.wikipedia.org/{link}" if link else ""
    return row

#this is a function that extract a row

def extract_all_row():
    # this function extracts all the table rows
    # the extract_single_row function was applied using the map function.
    #rows = get_data()[1:]
    data = list(map(extract_single_row,get_data()[1:]))
    return data

def to_csv():
    # the function writes the extracted data into a csv
    with open(csv_file,action,newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(extract_column_header())
        csv_writer.writerows(extract_all_row())

def to_json():
    # the function writes the extracted data into a json file
    with open(json_file,action) as f:
        json.dump(extract_all_row(), f, indent=5)
        # the 5 is the indentation to make it more readable


def transformation():
    '''
    this is the data transformation stage for the ETL process 
    before the data cleaning and tranformation process start, the data was explored.
    during data exploration, different errors were discovered.
    these errors were cleaned accordingly using the codes below.

    '''

    df = pd.read_csv("universities-data.csv",encoding="latin-1")

    # the founded column consist of an inconsistent value of "1833[34]"
    # the cleaning is done using regex function by first converting the series dtype into str,
    # then extract the first 4 digit.
    # finally the column data type was changed into integer.
    df["Founded"] = df["Founded"].str.extract("(\d{4})")
    df["Founded"] = df["Founded"].astype(int)

    #there're two incorrect values in the enrollment column
    #'18 911' and '1,045,665 (total) as per 2019/2020[14]\n311,028 (active) as per 4 November 2020 [15]'
    df["Enrollment"] = df["Enrollment"].str.replace(" ",",")
    df["Enrollment"] = df["Enrollment"].str.extract("(\d{1,3}(?:,\d{1,3})*)")
    df["Enrollment"] = df["Enrollment"].str.replace(",","")
    df["Enrollment"] = df["Enrollment"].astype(int)

    # saving the final df into a csv file.
    df.to_csv("universities-clean_data.csv",index=False)

'''
This is the final stage of the ETL pipeline
the transformed data is loaded into 2 databases: Postgres and Mysql

'''
# Loading data into Postgres DB
def postgres_Loading():
    df =  pd.read_csv("universities-clean_data.csv")
    logging.info("Attempting to connect to the database for uploading data.")
    engine = create_engine(f"postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_DB}",pool_recycle=3600, echo=False)
    try:        
        logging.info(f"Uploading data to table: {table_name}")
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Data uploaded successfully to {table_name}.")
    
        print("Data successfully written to database")
    except Exception as e:
        print(f"An error occurred: {e}")
    
# Loading data into Mysql DB
def Mysql_loading():
    df = pd.read_csv("universities-clean_data.csv")
    try:
        logging.info("Attempting to connect to the database for uploading data.")
        engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_DB}",pool_recycle=3600, echo=False)
        logging.info(f"Uploading data to table: {table_name}")
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Data uploaded successfully to {table_name}.")
        print("Data successfully written to database")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # this is the final main function to orchestrate the ETL process
    logging.info("starting ETL process...")
    logging.info("starts data extraction..")
    get_data()
    logging.info("html data downloaded..")
    extract_column_header()
    #extract_single_row()
    extract_all_row()
    logging.info("ALL rows are extracted")
    logging.info("started writing to csv...")
    to_csv()
    logging.info("finished writing into csv.")
    logging.info("started writing to json...")
    to_json()
    logging.info("finished writing into json.")
    logging.info("Data Transformation started...")
    transformation()
    logging.info("Data Transformation done...")
    logging.info("Starting Data Loading..")
    logging.info("Loading data into PostgresDB")
    postgres_Loading()
    logging.info("Data successfully loaded.")
    logging.info("Loading data into MysqlDB")
    Mysql_loading()
    logging.info("Data successfully loaded.")
    logging.info("ETL process done!")

if __name__ == '__main__':
    main()