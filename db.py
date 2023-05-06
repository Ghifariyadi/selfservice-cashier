import sqlite3

conn = sqlite3.connect("cashier.db")

cursor = conn.cursor()

sql_create_table = """
CREATE TABLE IF NOT EXISTS transaction (
    no INTEGER,
    Nama_Barang TEXT,
    Harga INTEGER,
    Jumlah INTEGER
); 
"""

cursor.execute(sql_create_table)

cursor.execute("SELECT * FROM transaction;")

for row in cursor.fetchall():
    print(row)