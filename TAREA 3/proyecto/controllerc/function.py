import pandas as pd
from configuracionc.app import App
from modelosc.model import CLIENT
from configuracionc.database import Database
from sqlite3 import Connection

def IngestDataProducts(app: App):
    conn = app.getConnection()
    bd = app.getDatabase()
    
    CreateTableCLIENT(conn)
    dataCLIENT = GetDatoSourceCLIENT()
    InsertDataCLIENT(bd, dataCLIENT)
    
    CreateTableVENTAS(conn)
    dataVentas = GetDatasourceOrders(conn)
    insertManyVentas(bd, dataVentas)
    
 

def GetDatoSourceCLIENT():
    pathData = '/workspaces/workspacepy2025/TAREA 3/proyecto/docusc/ventas2025.xls'
    df = pd.read_excel(pathData, sheet_name="ventas", engine='xlrd')
    return df

def CreateTableCLIENT(conn: Connection):
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS CLIENT')
    cursor.execute('''
        CREATE TABLE CLIENT (
            INVOICENUMBER INTEGER,
            QUANTITY INTEGER
        )
    ''')
    conn.commit()

def InsertDataCLIENT(bd: Database, data):
    # Eliminar duplicados basados en 'INVOICENUMBER'
    data = data.drop_duplicates(subset=['INVOICENUMBER'])
    data = data[['INVOICENUMBER', 'QUANTITY']]  # Seleccionar solo las columnas necesarias
    bd.insert_many('CLIENT', ['INVOICENUMBER', 'QUANTITY'], data)

def GetDatasourceOrders(conn):
    pathData = "/workspaces/workspacepy2025/TAREA 3/proyecto/docusc/ventas2025.xls"
    df = pd.read_excel(pathData, sheet_name="ventas", engine='xlrd')
    df_products = pd.read_sql_query("SELECT INVOICENUMBER, QUANTITY FROM CLIENT", conn)
    df_orders = df[['INVOICENUMBER', 'CLIENT', 'ITEMID']].dropna().drop_duplicates()
    df_orders['CLIENT'] = df_orders['CLIENT'].astype(str)
    print('shape orders', df_orders.shape)
    df_newOrders = df_orders.merge(df_products, how="left", left_on="INVOICENUMBER", right_on="INVOICENUMBER")
    df_newOrders = df_newOrders.drop_duplicates()
    print('shape orders 1', df_newOrders.shape)
    df_newOrders = df_newOrders[['INVOICENUMBER', 'CLIENT', 'QUANTITY', 'ITEMID']]
    list_tuples = [tuple(x) for x in df_newOrders.to_records(index=False)]
    return list_tuples

def insertManyVentas(bd: Database, data):
    bd.insert_many('VENTAS', ['ORDERID', 'CLIENT', 'QUANTITY', 'ITEMID'], data)

def CreateTableVENTAS(conn: Connection):
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS VENTAS')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS VENTAS (
            ORDERID TEXT PRIMARY KEY,
            CLIENT TEXT,
            QUANTITY INTEGER,
            ITEMID TEXT
        )
    ''')
    conn.commit()



