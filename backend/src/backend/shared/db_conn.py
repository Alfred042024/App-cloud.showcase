from backend.shared import config_env
from psycopg_pool import ConnectionPool 
from psycopg import Connection

DB_POOL = ConnectionPool(config_env.DB_URL, max_size=10, open=True )






