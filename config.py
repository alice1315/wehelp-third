import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_CONFIG = {
    'user': os.getenv("rds_user"), 
    'password': os.getenv("rds_password"),
    'host': 'wehelp.czi2w7686f8d.us-east-1.rds.amazonaws.com',
    'database': 'wehelp_third'
}
