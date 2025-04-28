import sqlite3

def conectadb():
    try:
        con = sqlite3.connect(rf"C:\Users\Eler\Desktop\projetoflask\db\usuarios.db")
        return con
    except:
        return None