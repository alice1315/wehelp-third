import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_CONFIG = {
    'user': os.getenv("rds_user"), 
    'password': os.getenv("rds_password"),
    'host': os.getenv("rds_host"),
    'database': 'wehelp_third'
}
