from backend.shared.db_conn import DB_POOL
from backend.models.urls_models import ADD_URLS_TYPE
from psycopg.rows import dict_row
from psycopg.errors import Error , UniqueViolation
from fastapi.exceptions import HTTPException
from fastapi.responses import Response

def get_url_by_id(id: int ): 
    with DB_POOL.connection() as connection: 
       connection.row_factory = dict_row

       res = connection.execute(
         "select * from urls where id = %s ", 
          params = [id] 
         ).fetchone()

       if res is not None: 
          return res
       else: 
          raise HTTPException(404 , "no data found with this id")

def get_url(): 
    with DB_POOL.connection() as connection: 
      connection.row_factory = dict_row

      res = connection.execute(
         "select * from urls"
     ).fetchall()

    if res is not None : 
        return res
    else: 
        return []
      
def add_new_url(body:ADD_URLS_TYPE): 
   try: 
        with DB_POOL.connection() as conn: 
            conn.row_factory = dict_row
            insert_result = conn.execute(
                "insert into urls (short_url,original_url) values (%s , %s) returning id as new_insert ", 
                params= (body.short_url, body.original_url)
                ).fetchone()
            return insert_result
        
   except UniqueViolation as err: 
        raise HTTPException(409, detail = [ "record già presente", "F0002"])
   except Error as err: 
       print(err)
       raise HTTPException(500, detail = ["Errore durante l'update", "F0001"])
       

def delete_url_service(id): 
    try:
        with DB_POOL.connection() as conn: 
            conn.row_factory = dict_row
            
            del_id= conn.execute(
                        "delete FROM urls where id = %s returning id as deleted_row_id",
                        params = (id,)
                        ).fetchone()
            
            if del_id is None  : 
              raise HTTPException(404, detail = [ "record non presente", "F0003"])
            else: 
                return None
    except Error as err: 
        raise HTTPException(500, detail = ["Errore durantel l'operazione", "F0006"])
    
            
