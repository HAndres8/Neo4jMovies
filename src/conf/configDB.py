from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()
URI=os.getenv("URI")
AUTH=(os.getenv("USR"), os.getenv("PWD"))

def connectionDB():
    try:
        driver = GraphDatabase.driver(uri=URI, auth=AUTH)
        return (driver)
    except Exception as ex:
        return ("Error:", ex.message)