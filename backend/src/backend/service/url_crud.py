from backend.shared.db_conn import DB_POOL
from models.urls_models import ADD_URLS_TYPE
from psycopg.rows import dict_row
from psycopg import Cursor

def get_url_by_id(id: int ): 
    with DB_POOL.connection() as connection: 
       connection.row_factory = dict_row

       res = connection.execute(
         "select * from urls where id = %s ", 
          id 
         ).fetchone()
       
    return res

def get_url(): 
    with DB_POOL.connection() as connection: 
      connection.row_factory = dict_row

      res = connection.execute(
         "select * from urls"
     ).fetchall()
      
    return res

def add_new_url(body:ADD_URLS_TYPE): 
   with DB_POOL.connection() as conn: 
      insert_result = conn.execute(
         "insert into urls (short_url,original_url) values (%s , %s)", 
         params= [body.short_url, body.original_url]
        ).results()
    

