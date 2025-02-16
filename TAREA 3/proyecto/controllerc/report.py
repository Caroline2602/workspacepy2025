from configuracionc.app import *
import pandas as pd

def GenerateReportVentas(app: App):
    conn = app.getConnection()
    query = """
        SELECT 
            v.CLIENT,
            v.ITEMID,
            SUM(v.QUANTITY) AS TOTALPRICE
        FROM 
            VENTAS v
        GROUP BY 
            v.CLIENT, v.ITEMID
        ORDER BY 
            TOTALPRICE DESC;
    """
    df = pd.read_sql_query(query, conn)
    fecha = "16-02"
    path = f"/workspaces/workspacepy2025/TAREA 3/proyecto/docusc/data2025-{fecha}.csv"
    df.to_csv(path)
    sendMail(app, path)

def sendMail(app: App, data):
    # cambiar el asunto 
    app.mail.send_email('9a3c8223168f67', 'caroline_2861899@outlook.com', 'Reporte de ventas', 'Adjunto el reporte de ventas', data)