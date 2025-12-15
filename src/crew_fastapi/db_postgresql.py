import psycopg2
import time

### OPEN CONNECTION
def open_connection():
    try:
        conn = psycopg2.connect(database = "postgres", 
                            user = "postgres", 
                            host= 'localhost',
                            password = "020411",
                            port = 5432)
        print("DB connected !")
        conn.commit()
    except:
        print("I am unable to connect to DB")
    return conn


### CREATE TABLE
def create_table():
    conn = open_connection()
    command = """ 
        CREATE TABLE IF NOT EXISTS analysis_history (
            code_id SERIAL PRIMARY KEY, 
            code_snippet TEXT NOT NULL,
            suggestion TEXT NOT NULL, 
            created_at VARCHAR(255) NOT NULL
        )"""
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            print("Table created")
            conn.commit()
            cur.close()
            
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    return conn
     

### INSERT TABLE
def insert_table(conn,code_snippet,suggestion):
    current_timestamp = str(time.time())
    tableInsert = " INSERT INTO analysis_history (code_snippet,suggestion,created_at) VALUES (\'" + code_snippet + "\', \'" + suggestion + "\', \'" + current_timestamp + "\') RETURNING code_id"

    try:
        with conn.cursor() as cur:
            cur.execute(tableInsert)
            rows = cur.fetchone()
            print("Table inserted")
            print(rows)
            conn.commit()
  
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    return conn
