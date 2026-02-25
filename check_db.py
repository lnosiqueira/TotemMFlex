import sqlite3

conn = sqlite3.connect("src/database/totem.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(interactions);")
columns = cursor.fetchall()

print("Colunas da tabela interactions:")
for col in columns:
    print(col)

conn.close()