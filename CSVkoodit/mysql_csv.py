import os
import csv
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def fetch_data(query):
    conn=mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    cur=conn.cursor()
    cur.execute(query)
    cols=[col[0] for col in cur.description]
    rows=cur.fetchall()
    cur.close()
    conn.close()
    return cols,rows

def save_csv(filename, cols, rows):
    with open(filename,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f, delimiter=';')
        writer.writerow(cols)
        for row in rows:
            writer.writerow(row)
def main():
    query = input("Anna SQL-kysely: ") #Select * from rawdata
    cols, rows = fetch_data(query)
    save_csv("db_output.csv", cols, rows)
    print("Tallennettu tiedostoon db_output.csv")

if __name__ == "__main__":
    main()            
