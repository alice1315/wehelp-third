import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_CONFIG = {
    'user': os.getenv("user"), 
    'password': os.getenv("password"),
    'host': 'wehelp.czi2w7686f8d.us-east-1.rds.amazonaws.com',
    'database': 'wehelp_third'
}
